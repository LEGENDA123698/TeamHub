from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.shortcuts import redirect
from auth_app.models import *
from portfolio_app.forms import *
from django.urls import reverse_lazy
from forum_app.models import Message
from portfolio_app.mixins import UserIsOwnerMixin, UserIsProfileOwner
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class ProfileView(DetailView):
    model = User
    template_name = 'portfolio/profile.html'

    def is_friend(self, user):
        if self.request.user.is_authenticated:
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

class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = ShowcaseElement
    form_class = ShowcaseElementForm
    template_name = 'portfolio/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('portfolio_app:user_profile', kwargs={'pk': self.request.user.id})
    
class PortfolioUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = ShowcaseElement
    form_class = ShowcaseElementForm
    template_name = 'portfolio/portfolio_update.html'
    
    def get_success_url(self):
        return reverse_lazy('portfolio_app:user_profile', kwargs={'pk': self.request.user.id})
    
class PortfolioDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = ShowcaseElement

    def get(self, request, *args, **kwargs):
        self.get_object().delete()
        return redirect('portfolio_app:user_profile', pk=self.request.user.id)

class FriendRequestsView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'portfolio/requests.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['requests'] = FriendRequest.objects.filter(receiver=user.id)
        return context

class ProfileUpdateView(LoginRequiredMixin, UserIsProfileOwner, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'portfolio/profile_update.html'
    context_object_name = 'user'
    
    def get_success_url(self):
        return reverse_lazy('portfolio_app:user_profile', kwargs={'pk': self.request.user.id})

@login_required
def friend_request(request, pk):
    if request.method == 'POST':
        if FriendRequest.objects.filter(sender=request.user, receiver=User.objects.get(id=pk)).exists():
            return redirect('portfolio_app:user_profile', pk=pk)
        
        FriendRequest.objects.create(sender=request.user, receiver=User.objects.get(id=pk))
    return redirect('portfolio_app:user_profile', pk=pk)

@login_required
def decline(request, pk):
    if request.method == 'POST':
        FriendRequest.objects.get(sender=pk, receiver=request.user).delete()
    return redirect('portfolio_app:friend_requests')

@login_required
def add_friend(request, pk):
    if request.method == 'POST':
        request.user.friends.add(User.objects.get(id=pk))
        FriendRequest.objects.get(sender=pk, receiver=request.user).delete()
    return redirect('portfolio_app:friend_requests')

@login_required
def delete_friend(request, pk):
    if request.method == 'POST':
        request.user.friends.remove(User.objects.get(id=pk))
    return redirect('portfolio_app:user_profile', pk=pk)