from django.conf import settings
from django.utils import timezone
from faker import Faker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from courses.factories import CourseFactory
from courses.models import Course
from users.models import User

COURSE_COUNT = 10
TEST_USER_USERNAME = 'usrname'
TEST_USER_PSW = 'vsafdadsfa34#'


class TestCaseForCity(APITestCase):

    def setUp(self):
        self.faker = Faker(locale=settings.LOCALE)
        user = User.objects.create_user(TEST_USER_USERNAME, TEST_USER_PSW)
        token, _ = Token.objects.get_or_create(user_id=user.id)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        [CourseFactory() for _ in range(COURSE_COUNT)]

    def test_get_courses_list(self):
        response = self.client.get("/api/courses/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(COURSE_COUNT, response.data["count"])
        self.assertEqual(COURSE_COUNT, len(response.data["results"]))

    def test_retrieve_course(self):
        course = Course.objects.first()
        response = self.client.get(f"/api/courses/{course.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(course.id, response.data["id"])

    def test_required_course_fields(self):
        course = Course.objects.first()
        response = self.client.get(f"/api/courses/{course.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        course_data = response.data
        required_course_fields = ['id', 'name', 'description', 'tutor_name',
                                  'is_active', 'lessons']
        for field in required_course_fields:
            self.assertTrue(field in course_data,
                            f"{field} should be in courses data. "
                            f"got {list(course_data.keys())}")

    def test_required_lesson_fields(self):
        course = Course.objects.first()
        response = self.client.get(f"/api/courses/{course.id}/")
        required_lesson_fields = ['id', 'name', 'description', 'date']
        lessons_data = response.data['lessons']
        self.assertTrue(lessons_data, 'lessons should be created by factory,'
        f'got {lessons_data}')
        lesson_data = lessons_data[0]
        for field in required_lesson_fields:
            self.assertTrue(field in lesson_data,
                            f"{field} should be in lesson data, "
                            f"got {list(lesson_data.keys())}")

    def test_patch_course_description(self):
        course = Course.objects.first()
        new_description = self.faker.text(max_nb_chars=50, ext_word_list=None)
        response = self.client.patch(f"/api/courses/{course.id}/",
                                     {'description': new_description})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.first().description, new_description)

    def test_course_creation(self):
        course_data = {
            'name': self.faker.text(max_nb_chars=50, ext_word_list=None),
            'description': self.faker.text(max_nb_chars=200,
                                           ext_word_list=None),
            'lessons': [
                {'name': self.faker.text(max_nb_chars=50, ext_word_list=None),
                 'description': self.faker.text(max_nb_chars=200,
                                                ext_word_list=None),
                 'date': timezone.now()}, ]}
        response = self.client.post(f"/api/courses/", course_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        lesson_data = course_data.pop('lessons')[0]
        for field, value in course_data.items():
            self.assertEqual(value, response.data[field])
        for field, value in lesson_data.items():
            self.assertEqual(value, response.data['lessons'][0])
