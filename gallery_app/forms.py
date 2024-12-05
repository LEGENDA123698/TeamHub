from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from trelloapp.models import *
from django import forms

#class UserForm (UserCreationForm):
    #class Meta(UserCreationForm.Meta):
    #model = User
    #fields = UserCreationForm.Meta.fields

#class UserAuthForm(AuthenticationForm):
    #class Meta:
        #model = User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commect
        fields = ['content']