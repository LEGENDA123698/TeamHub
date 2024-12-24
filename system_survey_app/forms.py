from django import forms
from system_survey_app.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_title']
        widgets = {
            'question_title': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть текст запитання...',
                'rows': 1,
            }),
        }
        labels = {
            'question_title': 'Текст питання',
        }
        

class MediaForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['media']
        widgets = {
            "media": forms.FileInput()
        }
        
class AddSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title_survey', 'description']
        
