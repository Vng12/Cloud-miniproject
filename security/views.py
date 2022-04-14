from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from .models import Security

# Create your views here.


class Historyview(ListView):
	model = Security
	template_name = 'viewer.html'