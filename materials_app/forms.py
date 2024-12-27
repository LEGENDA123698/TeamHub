from materials_app.models import *
from django import forms


class LinkForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['description', 'link']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter URL'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link'].required = True

class VideoForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['description', 'link']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter video URL'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link'].required = True

class FileForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['description', 'file']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].required = True

class ImageForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['description', 'image']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True
