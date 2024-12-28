from typing import Any
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.views.generic import *
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from datetime import timedelta
from django.utils.timezone import now


class SectionListView(ListView):
    model = Section
    context_object_name = "sections"
    template_name = "forum_app/start_page.html"

class SectionDetailView(DetailView):
    model = Section
    context_object_name = "sections"
    template_name = "forum_app/section_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['themes'] = self.object.section_theme.all()
        return context

class ThemeDetailView(DetailView):
    model = Theme
    context_object_name = "themes"
    template_name = "forum_app/theme_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['messages'] = self.object.message_set.all().order_by('-created_at')
        context['form'] = MessageForm()
        paginator = Paginator(context['messages'], 4)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Вы должны быть авторизованы для отправки сообщений.")
        
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.related_theme = self.object
            message.message_author = request.user
            message.save()
            return redirect(reverse('forum_app:theme_detail', args=[self.object.pk]))
        return self.get(request, *args, **kwargs)


    
#-----------------------------------------------------------------
    
class SectionCreateView(CreateView):
    model = Section 
    fields = ['name', 'tag', 'tag_color']
    success_url = reverse_lazy('forum_app:forum-start')

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)

class SectionDeleteView(DeleteView):
    model = Section
    success_url = reverse_lazy('forum_app:forum-start')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class SectionUpdateView(UpdateView):
    model = Section
    fields = ['name', 'tag', 'tag_color']
    success_url = reverse_lazy('forum_app:forum-start')

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)

#-----------------------------------------------------------------

class ThemeCreateView(CreateView):
    model = Theme
    fields = ['name', 'tag', 'tag_color'] 
    template_name = 'forum_app/section_detail.html'

    def form_valid(self, form):
        section_pk = self.kwargs.get('section_pk')
    
        try:
            theme_section = Section.objects.get(pk=section_pk)
        except Section.DoesNotExist:
            return redirect('forum_app:section_list')
        theme_author = self.request.user
        theme = form.save(commit=False)
        theme.section = theme_section
        theme.author = theme_author
        theme.related_section = theme_section
        theme.save()
        return redirect('forum_app:section_detail', pk=theme.section.pk)

class ThemeDeleteView(DeleteView):
    model = Theme

    def get_success_url(self):
        return reverse('forum_app:section_detail', kwargs={'pk': self.object.section.pk})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)
    
    
class ThemeUpdateView(UpdateView):
    model = Theme
    fields = ['name', 'tag', 'tag_color']

    def get_success_url(self):
        if self.object.section:
            return reverse('forum_app:section_detail', args=[self.object.section.pk])
        return reverse_lazy('forum_app:forum-start')


#-----------------------------------------------------------------

class MessageCreateView(CreateView):
    model = Message
    context_object_name = "message"
    template_name = ""

class MessageDeleteView(DeleteView):
    model = Message
    context_object_name = "message"

    def get_success_url(self):
        return reverse('forum_app:theme_detail', kwargs={'pk': self.object.related_theme.pk})


class MessageUpdateView(UpdateView):
    model = Message
    context_object_name = "message"
    fields = ['text', 'image']
    template_name = 'forum_app/message_form.html'

    def get_success_url(self):
        return reverse('forum_app:theme_detail', kwargs={'pk': self.object.related_theme.pk})
