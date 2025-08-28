from django.shortcuts import render
from django.views.generic import ListView
from .models import Task, Comment # Припустимо, у вас є модель Post
# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'