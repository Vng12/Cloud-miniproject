from django.shortcuts import render
from django.views.generic import ListView
from .models import notice

# Create your views here.


class Homepageview(ListView):
	model = notice
	template_name = 'notice.html'
