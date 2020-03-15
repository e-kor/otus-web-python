# Create your tests here.
import json

from graphene_django.utils.testing import GraphQLTestCase

from coursera.schema import schema
from users.factories import TutorFactory, StudentFactory


class GQLTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_tutors_query(self):
        response = self.query(
            '''
           query{
              tutors{
                        id
                      }
                }
            ''',
            op_name='tutors'
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_tutor_query(self):
        tutor = TutorFactory()
        response = self.query(
            '''
            query{
               tutor (id: %d){
                         id
                       }
                 }
             ''' % tutor.id,
            op_name='tutors'
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertEqual(tutor.id, int(content['data']['tutor']['id']))

    def test_students_query(self):
        response = self.query(
            '''
           query{
              students{
                        id
                      }
                }
            ''',
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_student_query(self):
        student = StudentFactory()
        response = self.query(
            '''
            query{
               student (id: %d){
                         id
                       }
                 }
             ''' % student.id,
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertEqual(student.id, int(content['data']['student']['id']))
