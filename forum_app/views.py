from typing import Any
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.views.generic import *
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator


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
        context['messages'] = self.object.theme_message.all()
        context['form'] = MessageForm()
        paginator = Paginator(context['messages'], 1)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.theme = self.object
            message.message_author = request.user
            message.save()
            return redirect(reverse('forum_app:theme_detail', args=[self.object.pk]))
        return self.get(request, *args, **kwargs)
    
#-----------------------------------------------------------------
    
class SectionCreateView(CreateView):
    model = Section 
    context_object_name = "section"
    template_name = ""

class SectionDeleteView(DeleteView):
    model = Section
    context_object_name = "section"
    template_name = ""

class SectionUpdateView(UpdateView):
    model = Section
    context_object_name = "section"
    template_name = ""

#-----------------------------------------------------------------

class ThemeCreateView(CreateView):
    model = Theme 
    context_object_name = "theme"
    template_name = ""

class ThemeDeleteView(DeleteView):
    model = Theme
    context_object_name = "theme"
    template_name = ""

class ThemeUpdateView(UpdateView):
    model = Section
    context_object_name = "theme"
    template_name = ""

#-----------------------------------------------------------------

class MessageCreateView(CreateView):
    model = Message
    context_object_name = "message"
    template_name = ""

class MessageDeleteView(DeleteView):
    model = Message
    context_object_name = "message"
    template_name = ""

    def dispatch(self, request, *args, **kwargs):
        message = self.get_object()
        if message.message_author != request.user:
            return HttpResponseForbidden("Вы не можете удалить это сообщение.")
        return super().dispatch(request, *args, **kwargs)

class MessageUpdateView(UpdateView):
    model = Message
    context_object_name = "message"
    template_name = ""

    def dispatch(self, request, *args, **kwargs):
        message = self.get_object()
        if message.message_author != request.user:
            return HttpResponseForbidden("Вы не можете редактировать это сообщение.")
        return super().dispatch(request, *args, **kwargs)