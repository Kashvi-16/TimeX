from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Timetable, Attendance, Substitution, Result
from django.contrib.auth import authenticate, login
import random
import cv2
from .forms import ResultForm
from .models import Result

# Login page view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'admin':
                return redirect('admin_dashboard')
            elif user.user_type == 'teacher':
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')
    return render(request, 'login.html')

# Admin Dashboard view
@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

# Teacher Dashboard view
@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

# Student Dashboard view
@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

# View for generating timetable using genetic algorithm
@login_required
def generate_timetable():
    # Initialize sample data for subjects and periods
    subjects = ['Math', 'Science', 'English', 'History', 'Physics', 'Chemistry']
    teachers = ['Teacher1', 'Teacher2', 'Teacher3', 'Teacher4']

    # Simulate timetable slots
    timetable_slots = []
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        for period in range(1, 7):
            subject = random.choice(subjects)
            teacher = random.choice(teachers)
            timetable_slots.append({
                'day': day,
                'period': period,
                'subject': subject,
                'teacher': teacher
            })

    return timetable_slots


# Facial recognition for teacher attendance
@login_required
def mark_teacher_attendance():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier('path_to_haarcascade.xml')

    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
            if len(faces) > 0:
                print("Attendance marked!")  # Replace with database logic
                break
        
        cv2.imshow('Attendance', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Result tabulation view
@login_required
def input_result(request):
    if request.user.user_type == 'teacher':
        if request.method == 'POST':
            form = ResultForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('input_result')  # Refresh page after submission
        else:
            form = ResultForm()
        return render(request, 'input_result.html', {'form': form})
    else:
        return redirect('login')

# View for students to see their results
@login_required
def view_student_result(request):
    if request.user.user_type == 'student':
        results = Result.objects.filter(student=request.user)
        return render(request, 'student_result.html', {'results': results})
    else:
        return redirect('login')
