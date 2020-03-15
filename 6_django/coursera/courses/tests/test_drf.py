from random import randint

from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course
from users.models import User

COURSE_COUNT = randint(1, 10)
TEST_USER_USERNAME = 'usrname'
TEST_USER_PSW = 'vsafdadsfa34#'


class TestCaseForCity(APITestCase):
    def setUp(self):
        user = User.objects.create_user(TEST_USER_USERNAME, TEST_USER_PSW)

    def test_auth(self):
        self.assertTrue(self.client.login(username=TEST_USER_USERNAME,
                                          password=TEST_USER_PSW))

    def test_get_city_api_client(self):
        courses = [Course() for _ in range(COURSE_COUNT)]
        response = self.client.get("/api/courses/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(COURSE_COUNT, response.get("count"))
