## Part 1: Creating initial app

1. Create a new Django project named `IntramuralLeagues`. Within this project add a new Django app entitled `intramurals`.

2. The two models in our app will be `Students` who have a first and last name and `Teams` who have a name. 

3. After creating our intial models and migrating our database. We should update the models file to have the appropriate many to many relationship since students can be part of more than one team and teams can have more than one student. Additionally, we should add in basic queries and the __str__ method for each model.

4. To save time we won't build out views and urls. Instead we will add students and teams through our admin panel. Create a new superuser account for yourself and add 2 teams and 4 students. *Make sure to require your models in admin.py so that they are accessible in the admin portal.*

Note: If you are having trouble creating students in the portal try running the following command in your shell to fix potential migration issues:

```git
python manage.py migrate --run-syncdb 
```

## Part 2: Intro to GraphQL

1. Should I rephrase this? "GraphQL is a query language for your API that uses a server-side runtime for executing queries with yor existing data. It provides a complete descriprtion of the data in your API and makes it easier to evolve APIs over time. GraphQL isn't tied to any specific database or storage engine and is instead backed by your existing code and data." We'll be implementing GraphQL in our app so that we avoid sending excessive and extraneous data included in most HTTP requests. The server will only send the exact resources and fields required by our query.

2. To get started with GraphQL we first need to install the correct tools in our shell:
```git
    pip install graphene-django
    pip install django-graphiql
```

3. We also need to add `graphene_django` to our list of INSTALLED_APPS in the settings.py file.

4. To be able to query our database we need to create a new schema.py file. GraphQL uses a graphical representation of our data as opposed to the typical hierarchical structure. To make this possible, Graphene needs to know about the types of the objects that will appear in the graph. We can set this up for student by copying the following into our schema.py file:

```python
# intramurals/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from intramurals.models import Student

class StudentType(DjangoObjectType):
    class Meta:
        model = Student
```
Following the same process add a class for TeamType to the file.

5. All queries need to happen through GraphQL's root type - the Query class. Let's provide the ability for a user to be able to list all of the students by adding this to the bottom of our schema.py file:

```python
class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)

    def resolve_all_students(self, info):
        return Student.objects.all()
```
Also add the ability for a user to query for a list of all the teams.

6. Lastly, we need to properly set the queryable schema as the very last line in schema.py:

```python
schema = graphene.Schema(query=Query)
```

7. To see and access the GraphiQL user interface we need to update our urls by adding graphql as a new route in our list of urlpatterns:

```python
 url(r'^graphql', GraphQLView.as_view(graphiql=True))
```
We also need to import the correct views at the top of urls.py:
```python
from graphene_django.views import GraphQLView
```

8. After updating urls, start up the server and go to the /graphql route. You should see the GraphiQL interface that we can use to practice testing our queries. In the top lefthand box type the following and press the play button to see the json representation of all the student ids and their first names.

```
query {
  allStudents {
    id, firstName
  }
}
```
As you type GraphiQL uses autocomplete to show you which fields are accessible in your queries. Try out some more queries yourself. Be able to query for a list of all the team names with the first names of the students on each of those teams.

9. Explanations of debugging? How to use query variables? etc.


