from django.shortcuts import render
from django.http import request
from django.contrib.auth import views
from django.contrib import auth
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
 
from django.http import HttpResponseRedirect
from .models import Post
def post_new(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    else: 
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.date = timezone.now()
                post.save()                
 
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
            return render(request, 'cheque/cheque.html', {'form': form})