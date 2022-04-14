from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('user_home')
		else:
			messages.info(request, 'invalid credentials')
			return redirect(request,'/')

	else:
		return render(request, 'signin user.html',{'linke':'http://127.0.0.1:8000/register','linke1':'http://127.0.0.1:8000/','linke2':'http://127.0.0.1:8000/about','linke3':'http://127.0.0.1:8000/contact','linke4':'http://127.0.0.1:8000/user_home'})

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				print("username already exists")
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save();
				print("user created")
				return redirect('login')
		else:
			print("password is not maching")
			return redirect('register')
		return redirect(reverse('/'))
	else:
		return render(request, 'getstarted.html',{'linkg1s':'http://127.0.0.1:8000/login'})
def logout(request):
	auth.logout(request)
	return redirect('/')