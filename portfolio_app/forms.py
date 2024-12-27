from django import forms
from portfolio_app.models import *

class ShowcaseElementForm(forms.ModelForm):
    class Meta:
        model = ShowcaseElement
        fields = ['image']

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'about']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
