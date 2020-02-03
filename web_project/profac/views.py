from django.shortcuts import render
from django.http import request
from django.http import HttpResponseRedirect


# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    else:
        return render(request, 'profac/profile.html')

def get_full_name(request):
    return {'request': request}


# Create your views here.
