from random import randint

import factory
from django.conf import settings
from factory.django import DjangoModelFactory
from faker import Faker
from pytz import utc

from courses.models import Course, Lesson, Tag
from users.factories import StudentFactory, TutorFactory
from users.models import Student

MAX_LESSONS_PER_COURSE = 10
MAX_STUDENTS_PER_COURSE = 100
LOCALE = settings.LOCALE
FAKER = Faker()


class TagFactory(DjangoModelFactory):
    name = factory.Faker('word',
                         locale=LOCALE)

    class Meta:
        model = Tag


class LessonFactory(DjangoModelFactory):
    name = factory.Faker('text', max_nb_chars=50, ext_word_list=None,
                         locale=LOCALE)
    description = factory.Faker('text', max_nb_chars=300, ext_word_list=None,
                                locale=LOCALE)
    date = factory.Faker('date_time', tzinfo=utc)

    class Meta:
        model = Lesson

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if extracted:
            self.tags.set(extracted)
        else:
            self.tags.set(
                FAKER.random_elements(Tag.objects.all() or [TagFactory()]))


class CourseFactory(DjangoModelFactory):
    name = factory.Faker('text', max_nb_chars=50, ext_word_list=None,
                         locale=LOCALE)
    description = factory.Faker('text', max_nb_chars=300, ext_word_list=None,
                                locale=LOCALE)
    tutor = factory.SubFactory(TutorFactory)

    class Meta:
        model = Course

    @factory.post_generation
    def lessons(self, create, extracted, **kwargs):
        for _ in range(randint(0, MAX_LESSONS_PER_COURSE)):
            LessonFactory(course=self)

    @factory.post_generation
    def students(self, create, extracted, **kwargs):
        if extracted:
            self.students.set(extracted)
        else:
            self.students.set(FAKER.random_elements(
                Student.objects.all() or [StudentFactory()]))

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if extracted:
            self.tags.set(extracted)
        else:
            self.tags.set(FAKER.random_elements(
                Tag.objects.all() or [TagFactory()], length=5))
