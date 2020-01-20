from django.shortcuts import render
from .forms import registrationForm
from django.contrib.auth.forms import  AuthenticationForm
from django.template import loader
from django.template import RequestContext
from django.http import HttpResponse

def custom_proc(request):
    return{
        'request': request,
    }


def registration(request):
    form = registrationForm()
    if request.method == 'POST':
        form = registrationForm(request.POST)   
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("main/home.html")
    c =  {'form': form}   
    return render(request, 'registration/registry.html', c)

