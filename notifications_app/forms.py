from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Notification
from django import forms

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['text', 'author', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
