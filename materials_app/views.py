from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from materials_app.forms import *
from django.shortcuts import get_object_or_404

class MaterialAddView(CreateView):

    template_name = 'materials/add_material.html'
    success_url = '/materials'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['options'] = ['ссылка', 'видео', 'файл', 'картинка']
        context['selected_option'] = self.request.GET.get('option')
        return context


class MaterialUpdateView(UpdateView):
    template_name = 'materials/update.html'
    success_url = '/materials'

    def get_form_class(self):
        value = self.kwargs.get('value')
        if value == 'link':
            return LinkForm
        elif value == 'video':
            return VideoForm
        elif value == 'file':
            return FileForm
        elif value == 'image':
            return ImageForm
        else:
            return LinkForm

    def get_queryset(self):
        value = self.kwargs.get('value')
        print('2', value)
        if value == 'link':
            return Link_Model.objects.all()
        elif value == 'video':
            return Video_Model.objects.all()
        elif value == 'file':
            return File_Model.objects.all()
        elif value == 'image':
            return Image_Model.objects.all()
        else:
            return Link_Model.objects.all()

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        return get_object_or_404(queryset, pk=pk)


class MaterialDeleteView(DeleteView):
    template_name = 'materials/delete.html'
    success_url = '/materials'

    def get_queryset(self):
        value = self.kwargs.get('value')
        if value == 'link':
            return Link_Model.objects.all()
        elif value == 'video':
            return Video_Model.objects.all()
        elif value == 'file':
            return File_Model.objects.all()
        elif value == 'image':
            return Image_Model.objects.all()
        else:
            return Link_Model.objects.all()

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        return get_object_or_404(queryset, pk=pk)


def materials_view(request):
    context = {
        'links': Link_Model.objects.all(),
        'videos': Video_Model.objects.all(),
        'files': File_Model.objects.all(),
        'images': Image_Model.objects.all(),
    }

    return render(
        request,
        template_name='materials/materials.html',
        context=context
    )