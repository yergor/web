from django.urls import path, include
from .views import all_cheques, add_cheque, cheque_detail
urlpatterns = [
    path('', add_cheque, name='add_cheque'),
    path('detail/<int:pk>/', cheque_detail, name='cheque_detail'),
    path('all_cheques/', all_cheques, name='all_cheques'),
    ]