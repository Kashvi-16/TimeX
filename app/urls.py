from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('admin/timetable/generate/', views.generate_timetable, name='generate_timetable'),
    path('teacher/attendance/', views.mark_teacher_attendance, name='mark_attendance'),
    path('teacher/input-result/', views.input_result, name='input_result'),
    path('student/view-result/', views.view_student_result, name='view_student_result'),
]
