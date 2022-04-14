from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django import forms

from .forms import CreateUserForm, ProfileRegisterForm
# Create your views here.
from django.http import HttpResponse
def home(request):
	return render(request, 'index.html',{'link':'http://127.0.0.1:8000/','link1':'http://127.0.0.1:8000/contact','link2':'http://127.0.0.1:8000/about','link3':'http://127.0.0.1:8000/login','link4':'http://127.0.0.1:8000/register','link5':'http://127.0.0.1:8000/admin/login/?next=/admin/'})
def contactus(request):
    if request.method == "POST":
        contact_name = request.POST['c_name']
        contact_email = request.POST['c_mail']
        contact_message = request.POST['c_message']
        send_mail(
            contact_name, # subject
            contact_message, # message
            contact_email, # from email
            ['soumyojyoti.datta@gmail.com'], # To Email
            )
        return render(request, 'contact.html', {'contact_name': contact_name})
    else:
        return render(request, 'contact.html')
def aboutus(request):
	return render(request, 'about.html',{'linka':'http://127.0.0.1:8000/','linka1':'http://127.0.0.1:8000/contact'})
def complaint(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['soumyojyoti.datta@gmail.com'], # To Email
            )
        return render(request, 'complaints.html', {'message_name': message_name})
    else:
        return render(request, 'complaints.html',{'linkcom1':'http://127.0.0.1:8000/user_home'})

#def signin(request):
	#return render(request, 'sign.html',{'linkb':'http://127.0.0.1:8000/','linkb1':'http://127.0.0.1:8000/about','linkb2':'http://127.0.0.1:8000/contact','linkb3':'http://127.0.0.1:8000/signin_user','linkb4':'http://127.0.0.1:8000/signin_admin'})
#def get_started(request):
	#return render(request, 'getstarted.html',{'linkg1s':'http://127.0.0.1:8000/sign-in'})




#def get_started(request):
  # form = CreateUserForm()
  # if request.method == 'POST':
  #    form = CreateUserForm(request.POST)
   #   if form.is_valid():
    #     user  = form.save()
   #      return redirect('user_home')
   # context = {'form' : form}
   # return render(request, 'getstarted.html', context)




##def get_started1(request):
	##return render(request, 'getstarted1.html',{'linkg1s': 'http://127.0.0.1:8000/sign-in'})

#def signadmin(request):
	#return render(request, 'signin admin.html',{'linkd':'http://127.0.0.1:8000/getstarted','linkd1':'http://127.0.0.1:8000/','linkd2':'http://127.0.0.1:8000/about','linkd3':'http://127.0.0.1:8000/contact','linked4':'http://127.0.0.1:8000/admin_home'})
#def signuser(request):
	#return render(request, 'signin user.html',{'linke':'http://127.0.0.1:8000/getstarted','linke1':'http://127.0.0.1:8000/','linke2':'http://127.0.0.1:8000/about','linke3':'http://127.0.0.1:8000/contact','linke4':'http://127.0.0.1:8000/user_home'})
#def adminhome(request):
	#return render(request, 'adminhome.htm',{'linkf':'http://127.0.0.1:8000/getstarted','linkf1':'http://127.0.0.1:8000/'})
def userhome(request):
	return render(request,'userhome.html',{'linkg':'http://127.0.0.1:8000/getstarted','linkg1':'http://127.0.0.1:8000/','linkg2':'http://127.0.0.1:8000/complain'})
""" lass Signup(View):
    def get(self, request):
        return render(request, 'signin user.html')


    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        # object creation
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            # print(first_name, last_name, phone, email, password)
            customer.password = make_password(
                customer.password)  # to hash the password
            customer.register()
            return redirect('user_home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signin user.html', data)
    # Vaidations

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 2:
            error_message = 'First Name must be 2 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 2:
            error_message = 'Last Name must be 2 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len(customer.email) < 4:
            error_message = 'Email must be 4 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
"""
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        p_reg_form = ProfileRegisterForm(request.POST)
        if form.is_valid() and p_reg_form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            p_reg_form = ProfileRegisterForm(request.POST, instance=user.profile)
            p_reg_form.full_clean()
            p_reg_form.save()
            messages.success(request, f'Your account has been sent for approval!')
            return redirect(reverse(''))
    else:
        form = CreateUserForm()
        p_reg_form = ProfileRegisterForm()
    context = {
        'form': form,
        'p_reg_form': p_reg_form
    }
    return render(request, '', context)





