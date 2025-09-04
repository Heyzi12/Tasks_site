from django.contrib import admin
from django.urls import path
from taskapp import views
urlpatterns = [
    path("", views.TaskListView.as_view(), name="Home"),
    path("create/", views.TaskCreateView.as_view(), name="create_task"),
    path("update/<int:pk>", views.TaskUpdateView.as_view(), name = "update_task"),
]