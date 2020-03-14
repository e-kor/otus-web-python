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
    tutor = graphene.Field(TutorType, id=graphene.Int())
    students = graphene.List(StudentType)
    student = graphene.Field(StudentType, id=graphene.Int())

    def resolve_tutors(self, *args, **kwargs):
        return Tutor.objects.all()

    def resolve_students(self, *args, **kwargs):
        return Student.objects.all()

    def resolve_tutor(self, info, **kwargs):
        if 'id' in kwargs:
            return Tutor.objects.get(id=kwargs['id'])

    def resolve_student(self, info, **kwargs):
        if 'id' in kwargs:
            return Student.objects.get(id=kwargs['id'])
