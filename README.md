# Django Quick Guide

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the Model-View-Controller (MVC) architectural pattern and emphasizes reusability and "pluggability" of components.

## Installation

To install Django, you can use pip:

```bash
pip install Django
```

## Creating a Project

To start a new Django project, use the command:

```bash
django-admin startproject projectname
```

This will create a new directory with the project name.

## Creating an App

In Django, a project can consist of multiple apps. To create an app:

```bash
python manage.py startapp appname
```

## Models

Models in Django are used to create tables in the database. A model is a class that inherits from `django.db.models.Model`.

```python
from django.db import models

class MyModel(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.IntegerField()
```

## Views

Views in Django are functions that take a web request and return a web response. This can be a HTML content, a redirect, a 404 error, an XML document, an image, or anything.

```python
from django.http import HttpResponse
from django.shortcuts import render

def my_view(request):
    return HttpResponse("Hello, World!")
```

## URLs

URLs in Django are used to map to views. You define these in a file called `urls.py`.

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
]
```

## Templates

Django uses a template language to generate dynamic HTML. You can use variables, tags and filters in your templates.

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Welcome to my website, {{ name }}!</h1>
</body>
</html>
```

## Admin Interface

Django comes with a built-in admin interface. To create a superuser for the admin interface, use the command:

```bash
python manage.py createsuperuser
```

## Running the Server

To start the Django development server:

```bash
python manage.py runserver
```

This is a very basic introduction to Django. For more detailed information, refer to the [official Django documentation](https://docs.djangoproject.com/).