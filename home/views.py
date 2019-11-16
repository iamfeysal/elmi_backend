from django.shortcuts import render
from users.models import AUTH_USER_MODEL
from django.views.generic import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"
