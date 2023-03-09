from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView
from .forms import BioForm
from .models import Bio

# Create your views here.

class Userhome(TemplateView):
    template_name="userhome.html"

class Profileview(TemplateView):
    template_name="profile.html"

class BioView(CreateView):
    form_class=BioForm
    template_name="addbio.html"
    success_url=reverse_lazy("pro")
    