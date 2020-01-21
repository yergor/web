from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.post_new, name='post_new'),]