from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("todo/", views.todo),
    path("todo/new/", views.todo_new),
    ]