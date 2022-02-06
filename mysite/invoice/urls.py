from django.urls import path
from .views import *

app_name = "invoice"
urlpatterns = [
    path('', InvoiceList.as_view(), name='list'),
    path('detail/<int:pk>', InvoiceDetail.as_view(), name='detail'),
    path('create/', InvoiceCreate.as_view(), name='create'),
    path('add_line/<int:pk>', InvoiceLineAdd.as_view(), name='add_line'),
]
