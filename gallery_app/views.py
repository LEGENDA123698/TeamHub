from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Image
from django.views.generic import *
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect

class GalleryStartView(TemplateView):
    template_name = 'gallery_app/gallery_start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        paginator = Paginator(context['images'], 20)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        return context

class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['title', 'image', 'grid_column_span', 'grid_row_span']
    success_url = reverse_lazy('gallery-start')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        page_number = (self.object.pk - 1) // 5 + 1 
        return redirect(f"{self.success_url}?page={page_number}")


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image
    fields = ['title', 'image', 'grid_column_span', 'grid_row_span']
    success_url = reverse_lazy('gallery-start')

    def test_func(self):
        image = self.get_object()
        return self.request.user == image.author

class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('gallery-start')

    def post(self, request, *args, **kwargs):
        image = self.get_object()
        image.image.delete()
        return super().post(request, *args, **kwargs)

    def test_func(self):
        image = self.get_object()
        return self.request.user == image.author
