from django.urls import path
from .views import *

app_name = "stock"
urlpatterns = [
    path('', StockEntryList.as_view(), name='list'),
    path('detail/<int:pk>', StockEntryDetail.as_view(), name='detail'),
    # path('edit/<int:pk>', StockEntryUpdate.as_view(), name='edit'),
    path('submit/<int:pk>', StockEntryUpdate.as_view(), {'process': 'submit'}, name='submit'),
    path('cancel/<int:pk>', StockEntryUpdate.as_view(), {'process': 'cancel'}, name='cancel'),
    path('create/', StockEntryCreate.as_view(), name='create'),

    path('add_line/', StockEntryLineCreate.as_view(), name='add_line'),
    path('edit_line/<int:pk>', StockEntryLineEdit.as_view(), name='edit_line'),
    path('delete_line/<int:pk>', StockEntryLineDelete.as_view(), name='delete_line'),
]
