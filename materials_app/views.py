from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from materials_app.forms import *
from materials_app.mixins import StaffRequiredMixin
from django.core.paginator import Paginator


class MaterialAddView(StaffRequiredMixin, CreateView):

    template_name = 'materials/add_material.html'
    success_url = '/materials/'

    def get_form_class(self):
        option = self.request.GET.get('option')
        if option == 'ссылка':
            return LinkForm
        elif option == 'видео':
            return VideoForm
        elif option == 'файл':
            return FileForm
        elif option == 'картинка':
            return ImageForm
        else:
            return LinkForm
        
    def form_valid(self, form):
        option = self.request.GET.get('option')
        if option == 'ссылка':
            form.instance.type = 'LINK'
        elif option == 'видео':
            form.instance.type = 'VIDEO'
        elif option == 'файл':
            form.instance.type = 'FILE'
        elif option == 'картинка':
            form.instance.type = 'IMAGE'
        else:
            form.instance.type = 'LINK'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['options'] = ['ссылка', 'видео', 'файл', 'картинка']
        context['selected_option'] = self.request.GET.get('option')
        return context


class MaterialUpdateView(StaffRequiredMixin, UpdateView):
    model = Material
    template_name = 'materials/update.html'
    success_url = '/materials/'

    def get_form_class(self, queryset=None):
        upd_obj = super().get_object(queryset)
        if upd_obj.type == 'LINK':
            return LinkForm
        elif upd_obj.type == 'VIDEO':
            return VideoForm
        elif upd_obj.type == 'FILE':
            return FileForm
        elif upd_obj.type == 'IMAGE':
            return ImageForm
        else:
            return LinkForm


class MaterialDeleteView(StaffRequiredMixin, DeleteView):
    model = Material

    def get(self, request, *args, **kwargs):
        self.get_object().delete()
        return redirect('materials_app:materials')


def materials_view(request):

    links = Material.objects.filter(type='LINK')
    videos = Material.objects.filter(type='VIDEO')
    files = Material.objects.filter(type='FILE')
    images = Material.objects.filter(type='IMAGE')

    page_number = request.GET.get('page')

    context = {
        'links': links,
        'videos': videos,
        'files': files,
        'images': images,
        'page_obj_links': Paginator(links, 4).get_page(page_number),
        'page_obj_videos': Paginator(videos, 4).get_page(page_number),
        'page_obj_files': Paginator(files, 4).get_page(page_number),
        'page_obj_images': Paginator(images, 4).get_page(page_number),
    }

    return render(
        request,
        template_name='materials/materials.html',
        context=context
    )