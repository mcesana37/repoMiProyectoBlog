from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='usuarios', default='default-user.png')
    
    def get_absolute_url(self):
        return reverse('home')
    