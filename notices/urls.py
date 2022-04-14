from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView
urlpatterns = [
    path('notice',views.Homepageview.as_view(),name='notice')]
