from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'registrations'
urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
  
]