from django.urls import path, include
from . import views
from django.conf.urls import url
urlpatterns = [
    path('rec/', views.rec, name='rec'),]