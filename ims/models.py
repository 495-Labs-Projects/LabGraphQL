from django.db import models

# Models

class Team(models.Model):
    # Team fields
    name = models.CharField(max_length=255)

    # Scopes/Manager
    class QuerySet(models.QuerySet):
        def alphabetical(self):
            return self.order_by("name")

    objects = QuerySet.as_manager()

    def __str__(self):
        return self.name


class Student(models.Model):
    # Student fields
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    teams = models.ManyToManyField(Team)

    # Scopes/Manager
    class QuerySet(models.QuerySet):
        def alphabetical(self):
            return self.order_by("last_name", "first_name")

    objects = QuerySet.as_manager()

    def __str__(self):
        return self.first_name + " " + self.last_name



