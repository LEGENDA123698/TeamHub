from django.shortcuts import render
from django.views.generic import *

class StartView(TemplateView):
    template_name = "main_app/start.html"

class EzvenenyaView(TemplateView):
    template_name = "main_app/ezvenenya.html"
