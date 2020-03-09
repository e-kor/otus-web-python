import graphene

from courses.schema import Mutation as CourseMutation, Query as CourseQuery
from users.schema import Query as UserQuery


class Query(CourseQuery, UserQuery, graphene.ObjectType): pass


class Mutation(graphene.ObjectType, CourseMutation): pass


schema = graphene.Schema(query=Query, mutation=Mutation)
