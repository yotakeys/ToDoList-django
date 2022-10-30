from django.shortcuts import render
from django.views.generic.list import ListView
from.models import Task

# Create your views here.


class TaskList(ListView):
    model = Task
    template_name = 'app/task_list.html'
    context_object_name = "tasks"
