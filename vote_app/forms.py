from django import forms
from vote_app.models import *


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter vote title'
            }),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = VoteAnswer
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter answer'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False