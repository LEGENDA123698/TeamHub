from django.shortcuts import render, redirect
from calendar_app.forms import *
from django.views.generic import CreateView, UpdateView, DeleteView
import calendar
from datetime import datetime
from django.core.paginator import Paginator
from calendar_app.mixins import StaffRequiredMixin


# создание
class EventCreateView(StaffRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'calendar/create.html'
    success_url = '/calendar/'

    def form_valid(self, form):
        form.instance.color = self.request.POST.get("color-select")
        return super().form_valid(form)

# обновление
class EventUpdateView(StaffRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'calendar/update.html'
    success_url = '/calendar/'

    def form_valid(self, form):
        form.instance.color = self.request.POST.get("color-select")
        return super().form_valid(form)

# удаление
class EventDeleteView(StaffRequiredMixin, DeleteView):
    model = Event

    def get(self, request, *args, **kwargs):
        self.get_object().delete()
        return redirect('calendar_app:calendar')


# основная страница календаря
def calendar_view(request):
    flat_list = list()
    today = datetime.today()
    year = request.GET.get('year', today.year)
    month = request.GET.get('month', today.month)
    
    try:
        year = int(year)
        month = int(month)
    except ValueError:
        year = today.year
        month = today.month

    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1

    cal = calendar.Calendar()
    flat_list = [day for week in cal.monthdayscalendar(year, month) for day in week]
    events = Event.objects.filter(date__year=year, date__month=month)

    days_with_events = list()
    for day in flat_list:
        events_for_day = events.filter(date__day=day)
        days_with_events.append({
            'day': day,
            'events': events_for_day
        })

    month_name = calendar.month_name[month]

    paginator = Paginator(events, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'events': events,
        'days_with_events': days_with_events,
        'month_name': month_name,
        'year': year,
        'month': month,
        'page_obj': page_obj,
    }

    return render(
        request,
        template_name='calendar/calendar.html',
        context=context
    )