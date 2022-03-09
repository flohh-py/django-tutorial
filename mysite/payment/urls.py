from django.urls import path
from .views import *

app_name = "payment"
urlpatterns = [
    path('', PaymentList.as_view(), name='list'),
    path('detail/<int:pk>', PaymentDetail.as_view(), name='detail'),
    path('edit/<int:pk>', PaymentUpdate.as_view(), name='edit'),
    path('submit/<int:pk>', PaymentUpdate.as_view(), {'process': 'submit'}, name='submit'),
    path('cancel/<int:pk>', PaymentUpdate.as_view(), {'process': 'cancel'}, name='cancel'),
    path('create/', PaymentCreate.as_view(), name='create'),

    path('add_line/', PaymentLineCreate.as_view(), name='add_line'),
    path('delete_line/<int:pk>', PaymentLineDelete.as_view(), name='delete_line'),
    path('edit_line/<int:pk>', PaymentLineEdit.as_view(), name='edit_line'),
]
