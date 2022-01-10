from django.urls import path
from .views import *

app_name = "invoice"
urlpatterns = [
    path('', InvoiceList.as_view(), name='list'),
    path('detail/<int:pk>', InvoiceDetail.as_view(), name='detail'),
]
