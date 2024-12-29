from django.shortcuts import render, redirect
from django.views.generic import DeleteView, TemplateView
from diary_app.forms import *
from diary_app.mixins import UserIsOwnerMixin, StaffRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


@method_decorator(staff_member_required, name='post')
class DiaryView(TemplateView):
    template_name = 'diary/diary.html'

    def get(self, request, user_pk=None):
        username = request.GET.get('username')
        if username:
            try:
                user = User.objects.get(username=username)
                if user.pk != user_pk:
                    return redirect('diary_app:diary', user_pk=user.pk)
            except User.DoesNotExist:
                return redirect('diary_app:diary', user_pk=user_pk)
        user = User.objects.get(pk=user_pk)
        context = self.get_context_data(user=user)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        theme_pk = kwargs.get('theme_pk')
        user_pk = kwargs.get('user_pk')
        theme_instance = None
        if theme_pk:
            try:
                theme_instance = Theme.objects.get(id=theme_pk, user=self.request.user)
            except Theme.DoesNotExist:
                return redirect('diary_app:diary', user_pk=user_pk)
            theme_form = ThemeForm(request.POST, instance=theme_instance)
        else:
            theme_form = ThemeForm(request.POST)
        note_form = NoteForm(request.POST)
        if theme_form.is_valid():
            theme_instance = theme_form.save(commit=False)
            if not theme_instance.pk:
                theme_instance.user = self.request.user
            theme_instance.save()
        if note_form.is_valid() and theme_instance:
            note_instance = note_form.save(commit=False)
            note_instance.user = User.objects.get(id=user_pk)
            note_instance.theme = theme_instance
            note_instance.save()
        return redirect('diary_app:diary', user_pk=user_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['themes'] = Theme.objects.all()
        context['diary_user'] = User.objects.get(id=self.kwargs.get('user_pk'))
        context['user'] = self.request.user
        context['theme_form'] = ThemeForm()
        context['note_form'] = NoteForm()
        return context
    
class ThemeDeleteView(StaffRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Theme

    def get(self, request, *args, **kwargs):
        self.get_object().delete()
        return redirect('diary_app:diary', user_pk=self.kwargs.get('user_pk'))
    
class NoteDeleteView(StaffRequiredMixin, DeleteView):
    model = Note

    def get(self, request, *args, **kwargs):
        self.get_object().delete()
        return redirect('diary_app:diary', user_pk=self.kwargs.get('user_pk'))