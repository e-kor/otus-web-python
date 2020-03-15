# Create your tests here.
import json

from django.conf import settings
from faker import Faker
from graphene_django.utils.testing import GraphQLTestCase

from coursera.schema import schema
from courses.factories import CourseFactory


class GQLTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    FAKER = Faker(locale=settings.LOCALE)

    def test_courses_query(self):
        response = self.query(
            '''
           query{
              courses{
                        id
                      }
                }
            ''',
            op_name='courses'
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_lessons_query(self):
        response = self.query(
            '''
           query{
              lessons{
                        id
                      }
                }
            ''',
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_course_mutation(self):
        course = CourseFactory()
        new_description = self.FAKER.text(max_nb_chars=300, ext_word_list=None)
        response = self.query(
            '''
           mutation {
              changeCourseDescription(courseId: %d, newDescription: "%s") {
                result
                course {
                  description
                }
              }
            }
            ''' % (course.id, new_description.replace('\n', '\\n')),
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertEqual(True,
                         content['data']['changeCourseDescription']['result'])
        self.assertEqual(new_description,
                         content['data']['changeCourseDescription']['course'][
                             'description'])
