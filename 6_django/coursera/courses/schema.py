import graphene
from graphene_django.types import DjangoObjectType

from .models import Course, Lesson


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class CourseMutation(graphene.Mutation):
    class Arguments:
        course_id = graphene.Int(required=True)
        new_description = graphene.String(required=True)

    result = graphene.Boolean()
    course = graphene.Field(CourseType)

    def mutate(self, info, course_id, new_description):
        course = Course.objects.get(id=course_id)
        course.description = new_description
        course.save()
        return {
            'result': True,
            'course': course}


class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson


class Mutation:
    change_course_description = CourseMutation.Field()


class Query:
    courses = graphene.List(CourseType)
    lessons = graphene.List(LessonType)

    def resolve_courses(self, *args, **kwargs):
        return Course.objects.all()

    def resolve_lessons(self, *args, **kwargs):
        return Lesson.objects.all()
