from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class PersonalUser(AbstractUser):
    #New data

    profile_photo = models.ImageField(upload_to = 'profiles/')
    personal_info = models.CharField(max_length = 200, blank = True)
    
