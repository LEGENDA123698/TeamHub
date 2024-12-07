from typing import Any
from django.shortcuts import render
from django.views.generic import *
from .models import *


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
        return context
    
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

class MessageUpdateView(UpdateView):
    model = Message
    context_object_name = "message"
    template_name = ""