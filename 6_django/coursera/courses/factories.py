import factory
from courses.models import Course, Lesson
from users.models import Tutor, Student
from users.factories import TutorFactory, StudentFactory
from django.conf import settings
from random import randint

MAX_LESSONS_PER_COURSE = 10
MAX_STUDENTS_PER_COURSE = 100
LOCALE = settings.LOCALE


class LessonFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('text', max_nb_chars=50, ext_word_list=None,
                         locale=LOCALE)
    description = factory.Faker('text', max_nb_chars=300, ext_word_list=None,
                                locale=LOCALE)
    date = factory.Faker('date_this_year')

    class Meta:
        model = Lesson


class CourseFactory(factory.django.DjangoModelFactory):
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
            [self.students.add(s) for s in extracted]
        else:
            for i in range(randint(0, MAX_STUDENTS_PER_COURSE)):
                self.students.add(StudentFactory())
