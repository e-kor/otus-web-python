from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import Student, Tutor


class Course(models.Model):
    title = models.CharField(max_length=50)
    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f"Course: {self.title}"


class Lesson(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    synopsis = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"Lesson {self.title} ({self.course})"
