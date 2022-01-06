from django.urls import path
from .views import *

app_name = "product"
urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('create/', ProductCreate.as_view(), name='create'),
    path('detail/<int:pk>', ProductDetail.as_view(), name='detail'),
    path('edit/<int:pk>', ProductUpdate.as_view(), name='edit'),
]
