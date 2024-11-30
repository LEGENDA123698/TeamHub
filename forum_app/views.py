from typing import Any
from django.shortcuts import render
from django.views.generic import *
from .models import *


class SectionListView(ListView):
    model = Section
    context_object_name = "section"
    template_name = "forum_app/start_page.html"

class SectionDetailView(DetailView):
    model = Section
    context_object_name = "section"
    template_name = "forum_app/section_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['themes'] = self.object.section_theme.all()
        return context

class ThemeDetailView(DetailView):
    model = Theme
    context_object_name = "theme"
    template_name = "forum_app/theme_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['messages'] = self.object.theme_message.all()
        return context