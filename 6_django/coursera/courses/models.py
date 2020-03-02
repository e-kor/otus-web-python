from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import Student, Tutor


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student, related_name='courses')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Course: {self.name}"


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='lessons')

    def __str__(self):
        return f"Lesson {self.name} ({self.course})"

    class Meta:
        ordering = ['date']
