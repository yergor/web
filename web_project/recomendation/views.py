from django.shortcuts import render
from django.http import request
from django.http import HttpResponseRedirect

# Create your views here.
def rec(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    else:
        return render(request, 'recomendation/recomendation.html')
    