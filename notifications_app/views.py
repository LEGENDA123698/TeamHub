from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import *

# Creation 
class NotificationCreateView(LoginRequiredMixin, CreateView):
    model = Notification
    fields = ['title', 'text', 'date']
    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'})
    }
    success_url = reverse_lazy('notifications_app:notifications-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update

class NotificationUpdateView(LoginRequiredMixin, UpdateView):
    model = Notification
    template_name = 'notification_app/notif_update.html'
    fields = ['title', 'text', 'date']
    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'})
    }
    success_url = reverse_lazy('notifications_app:notifications-list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

 
# Delete

class NotificationDeleteView(LoginRequiredMixin, DeleteView):
    model = Notification
    template_name = 'notification_app/notif_delete.html'
    success_url = reverse_lazy('notifications_app:notifications-list')


class NotificationListView(ListView):
    model = Notification
    template_name = 'notification_app/notif.html'
    context_object_name = 'notifications'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifications'] = Notification.objects.all()
        paginator = Paginator(context['notifications'], 2)
        page_num = self.request.GET.get('page')
        context['page_object'] = paginator.get_page(page_num)
        return context

class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'notification_app/notif_detail.html'
    context_object_name = 'notification'

