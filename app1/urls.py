"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('notices/', include('notices.urls')),
    path('security', include('security.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.home, name='home page'),
    path('contact',views.contactus, name='contact-us'),
    path('about',views.aboutus, name='about-us'),
   #path('sign-in',views.signin, name='sign-in'),
    #path('getstarted',views.get_started, name='getstarted'),
    #path('getstarted1',views.get_started1, name='getstarted1'),
    #path('signin_user',views.signuser,name='signin_user'),
    path('user_home',views.userhome,name='user_home'),
    path('complain',views.complaint,name='complain')

]
