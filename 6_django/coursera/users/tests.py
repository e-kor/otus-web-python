# Create your tests here.
import json

from graphene_django.utils.testing import GraphQLTestCase

from coursera.schema import schema


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

    def test_students_query(self):
        response = self.query(
            '''
           query{
              students{
                        id
                      }
                }
            ''',
            op_name='students'
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
