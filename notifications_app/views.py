from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


#def is_admin_or_moderator(user):
    #return user.is_superuser or user.groups.filter(name='Moderators').exists()

# Creation 
class NotificationCreateView(LoginRequiredMixin, CreateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_app/create_notif.html'
    success_url = '/notifications/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update

class NotificationUpdateView(LoginRequiredMixin, UpdateView):
    model = Notification
    fields = ['text']
    form_class = NotificationForm
    template_name = 'notification_app/update_notif.html'
    success_url = '/notifications/'

# Delete


class NotificationDeleteView(LoginRequiredMixin, DeleteView):
    model = Notification
    template_name = 'notification_app/delete_notif.html'
    success_url = '/notifications/'


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

