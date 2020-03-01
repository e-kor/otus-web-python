from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Tutor(User):
    def __str__(self):
        return f"Tutor {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Tutor'


class Student(User):
    def __str__(self):
        return f"Student {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Student'

