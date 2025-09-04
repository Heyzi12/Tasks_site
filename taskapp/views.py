from django.shortcuts import render
from django.views.generic import ListView , CreateView , UpdateView
from .models import Task, Comment
from django.urls import reverse_lazy # Припустимо, у вас є модель Post
# Create your views here.
from taskapp.forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_created.html'
    form_class = TaskForm
    success_url = reverse_lazy("Home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_edit.html'
    form_class = TaskForm
    success_url = reverse_lazy("Home")
    
