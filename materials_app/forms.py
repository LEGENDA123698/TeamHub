from materials_app.models import *
from django import forms


class LinkForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['description', 'link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link'].required = True

class VideoForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['description', 'link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link'].required = True

class FileForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['description', 'file']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].required = True

class ImageForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['description', 'image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True