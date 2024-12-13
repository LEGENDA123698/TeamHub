from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Image

class GalleryStartView(TemplateView):
    template_name = 'gallery_app/gallery_start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        return context
