from django.shortcuts import render
from django.http import request
from django.contrib.auth import views
from django.contrib import auth

from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    else:
        return render(request, 'main/home.html') 
def login(request):
    return render(request, "accounts/login.html")