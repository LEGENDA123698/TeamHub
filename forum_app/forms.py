from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'image']
        
    image = forms.ImageField(required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),label="Прикрепить изображение")
