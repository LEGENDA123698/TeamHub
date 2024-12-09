from django import forms
from portfolio_app.models import *

class ShowcaseElementForm(forms.ModelForm):
    class Meta:
        model = ShowcaseElement
        fields = ['image']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'about']