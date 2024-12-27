from auth_app.models import User
from django.db import models


class Survey(models.Model):
    title_survey = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title_survey


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_title = models.TextField()
    
    def __str__(self):
        return self.question_title


class Answer(models.Model):
    connection_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="answers", on_delete=models.CASCADE)
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to="comments_media/", blank=True, null=True)
    

    def __str__(self):
        return f"Відповіді на '{self.connection_question.survey}' від {self.user.username}"
    
    def get_absolute_url(self):
        return self.task.get_absolute_url()