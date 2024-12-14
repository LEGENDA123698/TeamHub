from django import forms
from vote_app.models import *


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['title']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = VoteAnswer
        fields = ['title', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False