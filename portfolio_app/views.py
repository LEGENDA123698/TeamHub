from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.shortcuts import redirect
from auth_app.models import *
from portfolio_app.forms import *
from django.urls import reverse_lazy
from forum_app.models import Message
from portfolio_app.mixins import UserIsOwnerMixin, UserIsProfileOwner


class ProfileView(DetailView):
    model = User
    template_name = 'portfolio/profile.html'

    def is_friend(self, user):
        if self.request.user.friends.filter(id=user.id).exists():
            return True

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        context['friends'] = user.friends.all()
        context['comments'] = Message.objects.filter(message_author=user)
        context['showcase_elements'] = user.showcase_elements.all()
        context['is_friend'] = self.is_friend(user)
        context['user'] = user
        return context

class PortfolioCreateView(CreateView):
    model = ShowcaseElement
    form_class = ShowcaseElementForm
    template_name = 'portfolio/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={'pk': self.request.user.id})
    
class PortfolioUpdateView(UserIsOwnerMixin, UpdateView):
    model = ShowcaseElement
    form_class = ShowcaseElementForm
    template_name = 'portfolio/update.html'
    
    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={'pk': self.request.user.id})
    
class PortfolioDeleteView(UserIsOwnerMixin, DeleteView):
    model = ShowcaseElement

    def get(self, request, *args, **kwargs):
        self.get_object().delete()
        return redirect('user_profile', pk=self.request.user.id)

class FriendRequestsView(TemplateView):
    model = User
    template_name = 'portfolio/requests.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['requests'] = FriendRequest.objects.filter(receiver=user.id)
        return context

class AvatarUpdateView(UserIsProfileOwner, UpdateView):
    model = User
    form_class = AvatarForm
    template_name = 'portfolio/update.html'
    
    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={'pk': self.request.user.id})

class ProfileUpdateView(UserIsProfileOwner, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'portfolio/update.html'
    
    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={'pk': self.request.user.id})

def friend_request(request, pk):
    if request.method == 'POST':
        FriendRequest.objects.create(sender=request.user, receiver=User.objects.get(id=pk))
    return redirect('user_profile', pk=pk)

def decline(request, pk):
    if request.method == 'POST':
        FriendRequest.objects.get(sender=pk, receiver=request.user).delete()
    return redirect('friend_requests')

def add_friend(request, pk):
    if request.method == 'POST':
        request.user.friends.add(User.objects.get(id=pk))
        FriendRequest.objects.get(sender=pk, receiver=request.user).delete()
    return redirect('friend_requests')

def delete_friend(request, pk):
    if request.method == 'POST':
        request.user.friends.remove(User.objects.get(id=pk))
    return redirect('user_profile', pk=pk)