from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from django.core.validators import MinLengthValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #confirmed = models.BooleanField("Confirmed", default=False)

    mobile = models.CharField("Mobile No", max_length=10, blank=True)
    tenantorowner = models.CharField("Tenant/owner", max_length=10, blank=True)
    block = models.CharField("Block No.", max_length=1, blank=True)
    flat = models.CharField("Flat No.", max_length=3, blank=True)


def __str__(self):
    return f'{self.user.username} Profile'


def save(self, *args, **kwargs):
    super().save(*args, **kwargs)


"""class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    Tenantorwner  = models.CharField(max_length=50)
    block = models.CharField(max_length=1)
    unit = models.CharField(max_length=5)

    #def register(self):
        #self.save()

    #to return the customer object based on the email provided
   # @staticmethod
   # def get_customer_by_email(email):
        #try:
           # return Customer.objects.get(email=email)
        #except:
           # return False

    #to check if the entered email is already registered into our database,if yes then show the required error message
   # def isExists(self):
       # if Registration.objects.filter(email = self.email):
            #return True
#  return  False"""






