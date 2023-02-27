from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.

class Userhome(TemplateView):
    template_name="userhome.html"

class Profileview(TemplateView):
    template_name="profile.html"