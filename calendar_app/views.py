from django.shortcuts import render
from calendar_app.forms import *
from django.views.generic import CreateView, UpdateView, DeleteView
import calendar
from datetime import datetime


# создание
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'calendar/create.html'
    success_url = '/calendar'

# обновление
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'calendar/update.html'
    success_url = '/calendar'

# удаление
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'calendar/delete.html'
    success_url = '/calendar'


# основная страница календаря
def calendar_view(request):
    today = datetime.today() #сегодняшняя дата
    year = today.year #текущий год
    month = today.month #текущий месяц
    cal = calendar.Calendar()
    flat_list = [item for sublist in cal.monthdayscalendar(year, month) for item in sublist] #список
    events = Event.objects.all()

    context = {
        'events': events,
        'date_list': flat_list,
        'year': year,
        'month': month,
    }

    return render(
        request,
        template_name='calendar/calendar.html',
        context=context
    )