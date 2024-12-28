from django.shortcuts import render
from vote_app.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import redirect
from django.forms import inlineformset_factory
from datetime import timedelta
from django.utils.timezone import now
from django.contrib.auth.mixins import LoginRequiredMixin
from vote_app.mixins import StaffRequiredMixin


class VoteCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Vote
    form_class = VoteForm
    template_name = 'vote/create.html'
    success_url = '/vote/'

    def get_answer_formset(self):
        current_extra = int(self.request.GET.get('extra', 2))
        if current_extra < 2:
            current_extra = 2
        return inlineformset_factory(Vote, VoteAnswer, form=AnswerForm, extra=current_extra, can_delete=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        AnswerFormSet = self.get_answer_formset()
        context['answer_formset'] = AnswerFormSet()
        context['current_extra'] = int(self.request.GET.get('extra', 2))
        return context

    def post(self, request, *args, **kwargs):
        vote_form = VoteForm(request.POST)
        AnswerFormSet = self.get_answer_formset()
        answer_formset = AnswerFormSet(request.POST, request.FILES)

        if vote_form.is_valid() and answer_formset.is_valid():
            vote = vote_form.save()
            answers = answer_formset.save(commit=False)
            for answer in answers:
                answer.vote = vote
                answer.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=vote_form, answer_formset=answer_formset))

class VoteUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Vote
    form_class = VoteForm
    template_name = 'vote/update.html'
    success_url = '/vote/'

    def get_answer_formset(self):
        return inlineformset_factory(Vote, VoteAnswer, form=AnswerForm, extra=0,)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        AnswerFormSet = self.get_answer_formset()
        context['obj'] = self.get_object()
        if self.request.POST:
            context['answer_formset'] = AnswerFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['answer_formset'] = AnswerFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        answer_formset = context['answer_formset']

        if answer_formset.is_valid():
            self.object = form.save()
            answer_formset.instance = self.object
            answer_formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class VoteDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Vote

    def get(self, request, *args, **kwargs):
        self.get_object().delete()
        return redirect('vote_app:votes')

class VotesView(ListView):
    model = Vote
    template_name = 'vote/votes.html'
    
class VoteDetailView(LoginRequiredMixin, DetailView):
    model = Vote
    template_name = 'vote/vote_detail.html'

    def all_voted_users(self):
        vote = self.get_object()
        answers = vote.vote_answers.all()
        value = 0
        for answer in answers:
            value += answer.user.count()
        return value
    
    def procent_count(self):
        vote = self.get_object()
        answers = vote.vote_answers.all()
        value = self.all_voted_users()
        if value != 0:
            for answer in answers:
                answer.procent = 100 * answer.user.count() / value
                answer.save()

    def post(self, request, *args, **kwargs):
        if now() > self.request.user.date_joined + timedelta(minutes=10):
            vote = self.get_object()
            answers = vote.vote_answers.all()
            if request.method == "POST":
                for answer in answers:
                    if answer.user.filter(id=self.request.user.id).exists():
                        answer.user.remove(self.request.user.id)
                selected_option = VoteAnswer.objects.get(id=request.POST.get('vote'))
                selected_option.user.add(self.request.user)
                return redirect('vote_app:detail_vote', pk=self.kwargs.get('pk'))
        else:
            return redirect('vote_app:votes')

    def get_context_data(self, **kwargs):
        vote = self.get_object()
        self.procent_count()
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        context['vote'] = vote
        context['answers'] = vote.vote_answers.all()
        return context
    
def remove_vote(request, pk):
    answer = VoteAnswer.objects.get(id=pk)
    if request.method == 'POST':
        answer.user.remove(request.user)
        vote = answer.vote
        answers = vote.vote_answers.all()
        total_users = sum(a.user.count() for a in answers)
        for a in answers:
            a.procent = 100 * a.user.count() / total_users if total_users > 0 else 0
            a.save()
    return redirect('vote_app:detail_vote', pk=answer.vote.id)

class Cat(TemplateView):
    template_name = 'vote/cat.html'