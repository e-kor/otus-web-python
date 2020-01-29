from django.contrib.auth.models import User
from django.db import models


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Course(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student)


class Lesson(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=1000, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
