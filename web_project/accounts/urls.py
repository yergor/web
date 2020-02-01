from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from registration.views import signup

app_name = 'registrations'
urlpatterns = [
    url('login', LoginView.as_view(), name='login'),
    url('logout', LogoutView.as_view(), name='logout'),
    url('signup/', signup, name='sigup'),
  
]