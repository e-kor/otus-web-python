from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Tutor(User):
    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = "Преподователи"


class Student(User):
    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = "Ученики"
