from . import views
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf.urls import url
from registration.views import signup

    
urlpatterns = [
     url(r'^login/$', LoginView.as_view(), name='login'),
     url('signup/', signup, name='signup'),
     url(r'^logout/$', LogoutView.as_view(next_page='/'), name='logout'),
]
