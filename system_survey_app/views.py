from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import *
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy
from django.urls import reverse


class SurveyListView(ListView):
    model = Survey
    template_name = 'system_survey_app/list_survey.html'
  
@method_decorator(login_required, name='dispatch')  
class SurveyDetailView(DetailView):
    model = Survey
    template_name = 'system_survey_app/detail_survey.html'

    def post(self, request, *args, **kwargs):
        survey = self.get_object()
        user = request.user

        # Удаляем старые ответы пользователя для текущего опроса
        Answer.objects.filter(
            connection_question__survey=survey,
            user=user
        ).delete()

        # Обработка новых ответов на вопросы
        questions = Question.objects.filter(survey=survey)

        for question in questions:
            answer_key = f"question_{question.id}"
            user_answer = request.POST.get(answer_key)

            if user_answer:
                Answer.objects.create(
                    connection_question=question,
                    user=user,
                    answer=user_answer
                )

        return redirect('detail-survey', pk=survey.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions"] = Question.objects.filter(survey=self.get_object())
        return context

    
    
class AddQuestionView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'system_survey_app/add_question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        survey_id = self.kwargs.get('pk')
        context['survey'] = Survey.objects.get(pk=survey_id)
        return context

    def form_valid(self, form):
        survey_id = self.kwargs.get('pk')
        survey = Survey.objects.get(pk=survey_id)
        form.instance.survey = survey
        form.save()
        return redirect('detail-survey', pk=survey.id)

      

class UserListView(ListView):
    model = User
    template_name = 'system_survey_app/list_users.html'

    def get_queryset(self):
        return User.objects.filter(answers__isnull=False).distinct()

class UserListSurveyView(ListView):
    model = Survey
    template_name = 'system_survey_app/user_list_surveys.html'

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        # Возвращаем уникальные опросы, которые прошёл пользователь
        return Survey.objects.filter(
            question__answer__user__id=user_id
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(id=self.kwargs['user_id'])
        context['user'] = user
        return context


    

@method_decorator(staff_member_required, name='dispatch')
class AddSurveyView(CreateView):
    form_class = AddSurveyForm
    template_name = 'system_survey_app/add_survey.html'
    success_url = reverse_lazy('list-surveys')
    

    
class UserDetailSurveyView(DetailView):
    model = Survey
    template_name = 'system_survey_app/user_detail_survey.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(id=self.kwargs['user_id'])
        answers = Answer.objects.filter(user=user, connection_question__survey=self.get_object())

        context['user'] = user
        context['survey'] = self.get_object()
        context['answers'] = answers
        
        return context
    


@method_decorator(staff_member_required, name='dispatch')
class UpdateQuestionView(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'system_survey_app/edit_question.html'

    def get_success_url(self):
        return reverse('detail-survey', kwargs={'pk': self.object.survey.pk})


@method_decorator(staff_member_required, name='dispatch')
class DeleteQuestionView(DeleteView):
    model = Question
    template_name = 'system_survey_app/confirm_delete.html'

    def get_success_url(self):
        return reverse('detail-survey', kwargs={'pk': self.object.survey.pk})


@method_decorator(staff_member_required, name='dispatch')
class DeleteSurveyView(DeleteView):
    model = Survey
    template_name = 'system_survey_app/confirm_delete.html'
    success_url = reverse_lazy('list-surveys')   
