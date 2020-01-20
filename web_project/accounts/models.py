from django.db import models
from django.contrib.auth.models import User, UserManager


class UserProfile(User):    
    name = models.EmailField(max_length=50,     blank=False,)   
    nickname = models.CharField(max_length=50,  blank=False,)       
    phone = models.CharField(max_length=50, blank=False,)

    objects = UserManager()