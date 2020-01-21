from django.urls import path, include
from . import views
import profac.views
import cheque.views
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('profile/', profac.views.index, name='profile'),
    path('cheque/', cheque.views.post_new, name='cheque'),
]