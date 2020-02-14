from django.urls import path, include
from . import views
from profac.views import profile
from cheque.views import add_cheque, all_cheques
from django.conf.urls import url
from registration.views import signup
from recomendation.views import rec
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('profile/', profile, name='profile'),
    path('cheque/', add_cheque, name='cheque'),
    url('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    url('signup/', signup, name='signup'),
    url('rec/', rec, name='rec'),
    path('all_cheques/', all_cheques, name='all_cheques'),
]