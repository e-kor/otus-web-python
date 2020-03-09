# Create your tests here.
import json

from graphene_django.utils.testing import GraphQLTestCase
from coursera.schema import schema


class GQLTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

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

