from django.urls import path
from .views import *

app_name = "stock"
urlpatterns = [
    path('', StockEntryList.as_view(), name='list'),
    path('detail/<int:pk>', StockEntryDetail.as_view(), name='detail'),
    path('create/', StockEntryCreate.as_view(), name='create'),
    path('add_line/<int:pk>', StockEntryLineAdd.as_view(), name='add_line'),
]
