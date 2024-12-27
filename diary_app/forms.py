from django import forms
from diary_app.models import *


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['title']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note', 'date', 'type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }