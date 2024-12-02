from materials_app.models import *
from django import forms


# форма для события
class LinkForm(forms.ModelForm):
    class Meta:
        model = Link_Model
        fields = ['description', 'link']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video_Model
        fields = ['description', 'link']

class FileForm(forms.ModelForm):
    class Meta:
        model = File_Model
        fields = ['description', 'file']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image_Model
        fields = ['description', 'image']