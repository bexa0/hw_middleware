from django.shortcuts import render
from django.views.generic import TemplateView


class StartView(TemplateView):
    template_name = 'app/start.html'
