# ims/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug
from ims.models import Student, Team

class StudentType(DjangoObjectType):
    class Meta:
        model = Student

class TeamType(DjangoObjectType):
    class Meta:
        model = Team

class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)
    all_teams = graphene.List(TeamType)

    # Debug field (rawSql, parameters etc).
    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_all_students(self, info):
        return Student.objects.all()

    def resolve_all_teams(self, info):
        return Team.objects.all()

schema = graphene.Schema(query=Query)