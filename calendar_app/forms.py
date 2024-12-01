from calendar_app.models import *
from django import forms


# форма для события
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date',]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }