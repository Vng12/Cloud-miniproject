from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView
urlpatterns = [
    path('security',views.Historyview.as_view(),name='security')]