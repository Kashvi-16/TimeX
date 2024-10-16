from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Student, Marks, Result


# Login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'password']

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'subject', 'internal_marks','external_marks','total_marks']


# Mark input form (used by teachers for adding marks)
class MarksForm(forms.ModelForm):
    assignment_marks = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Assignment Marks'}))
    midterm_marks = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Midterm Marks'}))
    practical_marks = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Practical Marks'}))
    final_marks = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Final Marks'}))

    class Meta:
        model = Marks
        fields = ['student', 'subject', 'assignment_marks', 'midterm_marks', 'practical_marks', 'final_marks']


# Additional form if needed for teacher substitution, attendance, etc.
# Example: Teacher Substitution Form (for admin/teacher to record substitutions)
class TeacherSubstitutionForm(forms.Form):
    teacher = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teacher Name'}))
    substitute_teacher = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Substitute Teacher'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'}))
    period = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Period'}))

