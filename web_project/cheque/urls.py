from django.urls import path, include
from .views import all_cheques, add_cheque, cheque_datail
urlpatterns = [
    path('', add_cheque, name='add_cheque'),
    path('datail', cheque_datail, name='cheque_datail'),
    path('all_cheques/', all_cheques, name='all_cheques'),
    path('ref', cheque_datail, name='ref'),
]