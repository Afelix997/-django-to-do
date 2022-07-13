from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("todo/", views.todo),
    path("todo/new/", views.todo_new),
    path("todo/<int:todo_id>/", views.todo_detail),
    path("todo/<int:todo_id>/edit/", views.todo_edit),
    path("todo/<int:todo_id>/edit_/", views.todo_edit_),
    path("todo/<int:todo_id>/delete/", views.todo_delete),
    ]