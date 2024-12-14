from django.shortcuts import render
from vote_app.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.forms import inlineformset_factory


class VoteCreateView(CreateView):
    model = Vote
    form_class = VoteForm
    template_name = 'vote/create.html'
    success_url = '/vote'
    AnswerFormSet = inlineformset_factory(Vote, VoteAnswer, form=AnswerForm, extra=4)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answer_formset'] = self.AnswerFormSet()
        return context

    def post(self, request, *args, **kwargs):
        vote_form = VoteForm(request.POST)
        answer_formset = self.AnswerFormSet(request.POST, request.FILES)

        if vote_form.is_valid() and answer_formset.is_valid():
            vote = vote_form.save()
            answers = answer_formset.save(commit=False)
            for answer in answers:
                answer.vote = vote
                answer.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=vote_form, answer_formset=answer_formset))

class VoteUpdateView(UpdateView):
    model = Vote
    form_class = VoteForm
    template_name = 'vote/update.html'
    success_url = '/vote'

    def post(self, request, *args, **kwargs):
        vote_form = self.get_form()
        if vote_form.is_valid():
            vote = vote_form.save()
            for answer in VoteAnswer.objects.filter(vote=vote):
                answer.save()
            return redirect(self.success_url)
        return self.form_invalid(vote_form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vote_form'] = VoteForm()
        context['answer_form'] = AnswerForm()
        context['answers'] = VoteAnswer.objects.filter(vote=self.get_object())
        return context


class VoteDeleteView(DeleteView):
    model = Vote
    template_name = 'vote/delete.html'
    success_url = '/vote'


class VotesView(ListView):
    model = Vote
    template_name = 'vote/votes.html'
    

class VoteDetailView(DetailView):
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
        vote = self.get_object()
        answers = vote.vote_answers.all()
        if request.method == "POST":
            for answer in answers:
                if answer.user.filter(id=self.request.user.id).exists():
                    answer.user.remove(self.request.user.id)
            selected_option = VoteAnswer.objects.get(id=request.POST.get('vote'))
            selected_option.user.add(self.request.user)
            return redirect('detail_vote', pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        vote = self.get_object()
        self.procent_count()
        context = super().get_context_data(**kwargs)
        context['vote'] = vote
        context['answers'] = vote.vote_answers.all()
        return context