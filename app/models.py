from django.db import models
from django.contrib.auth.models import AbstractUser

# Extend Django's default user model to include roles
class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Avoids conflict with the default 'user_set'
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Avoids conflict with the default 'user_set'
        blank=True
    )

class Timetable(models.Model):
    day = models.CharField(max_length=10)
    period = models.IntegerField()
    subject = models.CharField(max_length=100)
    created_by = models.ForeignKey('User', related_name='created_timetables', on_delete=models.CASCADE)
    teacher = models.ForeignKey('User', related_name='teacher_timetables', on_delete=models.CASCADE)

class Attendance(models.Model):
    teacher = models.ForeignKey(User, limit_choices_to={'user_type': 'teacher'}, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField()

class Substitution(models.Model):
    original_teacher = models.ForeignKey(User, related_name='original_teacher', on_delete=models.CASCADE)
    substitute_teacher = models.ForeignKey(User, related_name='substitute_teacher', on_delete=models.CASCADE)
    date = models.DateField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    # any other fields for Student


class Marks(models.Model):
    student = models.ForeignKey('app.Student', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField()
    
    def __str__(self):
        return f"{self.student} - {self.subject}"

class Result(models.Model):
    student = models.ForeignKey(User, limit_choices_to={'user_type': 'student'}, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    internal_marks = models.FloatField()
    external_marks = models.FloatField()
    total_marks = models.FloatField()

    # Automatically calculate total marks when saving
    def save(self, *args, **kwargs):
        self.total_marks = self.internal_marks + self.external_marks
        super(Result, self).save(*args, **kwargs)

