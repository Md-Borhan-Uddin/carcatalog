from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from accounts.managers import UserManager
# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(("Email"), max_length=254, unique=True)
    phone_number = models.CharField(('Phone Number'),max_length=11, unique=True)
    image = models.ImageField(("Profile Image"), upload_to='profile/image', height_field=100, width_field=100, null=True,blank=True)
    create = models.DateTimeField(("Create"),auto_now_add=True)
    update = models.DateTimeField(("Update"),auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return reverse("userdetail", kwargs={"pk": self.pk})
    