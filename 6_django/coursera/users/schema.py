import graphene
from graphene_django.types import DjangoObjectType

from .models import Student, Tutor


class TutorType(DjangoObjectType):
    class Meta:
        model = Tutor


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query:
    tutors = graphene.List(TutorType)
    students = graphene.List(StudentType)

    def resolve_tutors(self, *args, **kwargs):
        return Tutor.objects.all()

    def resolve_students(self, *args, **kwargs):
        return Student.objects.all()
