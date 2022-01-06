from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductList.as_view(), name='products_list'),
    path('create/', ProductCreate.as_view(), name='products_create'),
]
