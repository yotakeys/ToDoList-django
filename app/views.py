from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class Login(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'app/task_list.html'
    context_object_name = "tasks"


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    Template_name = 'app/task_detail.html'
    context_object_name = "task"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'app/task_create.html'


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'app/task_update.html'


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'app/task_delete.html'
