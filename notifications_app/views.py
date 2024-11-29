from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

class NotificationCreateView(CreateView):
    model = Notification
    form_class = NotificationForm
    
class NotificationUpdateView(UpdateView):
    model = Notification
    form_class = NotificationForm

class NotificationDeleteView(DeleteView):
    model = Notification