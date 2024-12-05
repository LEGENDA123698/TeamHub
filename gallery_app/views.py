from django.shortcuts import render, redirect
from trelloapp import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import *


# Create your views here.

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'trelloapp/task_list.html'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'trelloapp/create_task.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'trelloapp/task_detail.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.post)
        form.instance.author = request.user
        form.instance.task = self.get_object()

        if form.is_valid:
            form.save()
            return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Commect.objects.all()
        return super().get_context_data(**kwargs)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'trelloapp/create_task.html'
    success_url = '/'

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'trelloapp/delete_task.html'

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'trelloapp/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

