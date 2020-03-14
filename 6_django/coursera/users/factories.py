import factory
from courses.models import Course, Lesson
from users.models import Tutor, Student
from django.conf import settings

LOCALE = settings.LOCALE


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name', locale=LOCALE)
    last_name = factory.Faker('last_name', locale=LOCALE)
    username = factory.Faker('user_name', locale=LOCALE)


class TutorFactory(UserFactory, factory.django.DjangoModelFactory):
    class Meta:
        model = Tutor


class StudentFactory(UserFactory, factory.django.DjangoModelFactory):
    class Meta:
        model = Student
