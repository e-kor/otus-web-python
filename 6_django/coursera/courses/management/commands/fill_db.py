import logging

from django.core.management import BaseCommand
from django.db import IntegrityError
from faker import Faker

from courses.factories import CourseFactory
from courses.models import Course, Lesson
from users.factories import StudentFactory, TutorFactory
from users.models import Student, Tutor

STUDENTS_COUNT = 500
TUTORS_COUNT = 10
COURSES_COUNT = 50
LESSONS_PER_COURSE_COUNT = 30
FAKER = Faker()


def clear_db():
    for cls in Tutor, Student, Course, Lesson:
        info = cls.objects.all().delete()
        logging.info('deleted all %s: %s', cls.__name__, info)


def fill_db():
    logging.info("started filling test db")
    for _ in range(STUDENTS_COUNT):
        try:
            StudentFactory()
        except IntegrityError:
            logging.warning("couldn't create due to integrity error")
    logging.info("created %s students", STUDENTS_COUNT)

    for _ in range(TUTORS_COUNT):
        TutorFactory()
    logging.info("created %s tutors", TUTORS_COUNT)

    for _ in range(COURSES_COUNT):
        CourseFactory(tutor=FAKER.random_element(Tutor.objects.all()),
                      students=FAKER.random_elements(Student.objects.all()))
    logging.info("created %s courses", COURSES_COUNT)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        clear_db()
        fill_db()
