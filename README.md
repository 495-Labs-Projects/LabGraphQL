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

1. Should I rephrase this? "GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools."

2. To get started with graphQL we first need to install the correct tools in our shell:
```git
    pip install graphene-django
    pip install django-graphiql
```

3. We also need to add `graphene_django` to our list of INSTALLED_APPS in the settings.py file.

4. To be able to query our database we need to create schema.py
etc....

5. To see the GraphiQL user interface we need to update our urls by adding graphql as a new route in our list of urlpatterns.

```python
 url(r'^graphql', GraphQLView.as_view(graphiql=True))
```
We also need to import the correct views:
```python
from graphene_django.views import GraphQLView
```

6. Now we can query our database!

```
query{
  allStudents {
    id, firstName
  }
}
```
