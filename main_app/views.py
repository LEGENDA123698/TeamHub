from django.shortcuts import render
from django.views.generic import *

class StartView(TemplateView):
    template_name = "main_app/start.html"