from django.urls import path, include
from . import views
import profac.views
import cheque.views
from django.conf.urls import url
from registration.views import signup
from recomendation.views import rec
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('profile/', profac.views.index, name='profile'),
    path('cheque/', cheque.views.post_new, name='cheque'),
    url('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    url('signup/', signup, name='signup'),
    url('rec/', rec, name='rec')
]