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

def add_cheque(request):
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
                return redirect('cheque_detail', pk=post.pk)
        else:
            form = PostForm()
            return render(request, 'cheque/cheque.html', {'form': form})
def cheque_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'cheque/cheque_datail.html', {'post': post})
def all_cheques(request):
    peopless = Post.objects.all()
    return render(request, 'cheque/all_cheques.html', locals())