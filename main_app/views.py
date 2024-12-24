from django.views.generic import *
from django.shortcuts import render
from django.db.models import Q
from forum_app.models import Section, Theme, Message
from gallery_app.models import Image
from calendar_app.models import Event


class StartView(TemplateView):
    template_name = "main_app/start.html"

<<<<<<< HEAD

class EzvenenyaView(TemplateView):
    template_name = "main_app/ezvenenya.html"

=======
>>>>>>> feature-forum
def global_search(request):
    query = request.GET.get('query', '').strip()
    results = {
        'forum_sections': [],
        'forum_themes': [],
        'forum_messages': [],
        'gallery_images': [],
        'calendar_events': []
    }
    
    if query:
        results['forum_sections'] = Section.objects.filter(
            Q(name__icontains=query) | Q(tag__icontains=query)
        )
        results['forum_themes'] = Theme.objects.filter(
            Q(name__icontains=query) | Q(tag__icontains=query) | Q(text__icontains=query)
        )
        results['forum_messages'] = Message.objects.filter(
            Q(text__icontains=query)
        )
        results['gallery_images'] = Image.objects.filter(
            Q(title__icontains=query) | Q(author__username__icontains=query)
        )
        results['calendar_events'] = Event.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    
    return render(request, 'search_results.html', {'query': query, 'results': results})
<<<<<<< HEAD
=======

class EzvenenyaView(TemplateView):
    template_name = "main_app/ezvenenya.html"
>>>>>>> feature-forum
