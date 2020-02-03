from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.add_cheque, name='add_cheque'),
    path('post/<int:pk>/', views.cheque_detail, name='post_detail'),
    path('all/', views.add_cheque, name='all_cheques'),
    ]