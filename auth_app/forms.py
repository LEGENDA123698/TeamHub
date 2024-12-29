from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User