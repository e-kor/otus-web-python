import logging

from django.core.management import BaseCommand
from faker import Faker
from transliterate import translit

from courses.factories import CourseFactory, LessonFactory
from users.factories import TutorFactory, StudentFactory
from courses.models import Course, Lesson
from users.models import Student, Tutor

STUDENTS_COUNT = 500
TUTORS_COUNT = 10
COURSES_COUNT = 50
LESSONS_PER_COURSE_COUNT = 30
FAKER = Faker(locale='ru_RU')


def clear_db():
    for cls in Tutor, Student, Course, Lesson:
        info = cls.objects.all().delete()
        logging.info('deleted all %s: %s', cls.__name__, info)


def create_student():
    first_name = FAKER.first_name()
    last_name = FAKER.last_name()
    username = '_'.join(
        [translit(v, reversed=True).lower() for v in (first_name, last_name,)])
    s = Student.objects.create(
        username=username + str(FAKER.pyint()),
        first_name=first_name,
        last_name=last_name
    )
    logging.debug("created student %s", s)
    return s


def create_tutor():
    first_name = FAKER.first_name()
    last_name = FAKER.last_name()
    username = '_'.join(
        [translit(v, reversed=True).lower() for v in (first_name, last_name)])
    t = Tutor.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name
    )
    logging.debug("created tutor %s", t)
    return t


def create_lesson(c: Course):
    l = Lesson.objects.create(
        date=FAKER.date_this_year(),
        name=FAKER.text(max_nb_chars=50, ext_word_list=None),
        description=FAKER.text(max_nb_chars=300, ext_word_list=None),
        course=c
    )
    logging.debug("created lesson %s", l)
    return l


def create_course():
    c = Course.objects.create(
        name=FAKER.text(max_nb_chars=20, ext_word_list=None),
        description=FAKER.text(max_nb_chars=300, ext_word_list=None),
        tutor=FAKER.random_element(Tutor.objects.all())
    )
    c.students.set(FAKER.random_elements(Student.objects.all()))
    for _ in range(LESSONS_PER_COURSE_COUNT):
        create_lesson(c)
    logging.debug("created course %s", c)
    return c


def fill_db():
    logging.info("started filling test db")
    for _ in range(STUDENTS_COUNT):
        StudentFactory()
    logging.info("created %s students", STUDENTS_COUNT)

    for _ in range(TUTORS_COUNT):
        TutorFactory()
    logging.info("created %s tutors", TUTORS_COUNT)

    for _ in range(COURSES_COUNT):
        CourseFactory(tutor = FAKER.random_element(Tutor.objects.all()),
                      students = FAKER.random_elements(Student.objects.all()))
    logging.info("created %s courses", COURSES_COUNT)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        clear_db()
        fill_db()
