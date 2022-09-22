from re import template
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    template_name='page/home.html'

class AboutView(TemplateView):
    template_name= 'page/about.html'