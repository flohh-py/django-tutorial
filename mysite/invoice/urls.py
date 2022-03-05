from django.urls import path
from .views import *

app_name = "invoice"
urlpatterns = [
    path('', InvoiceList.as_view(), name='list'),
    path('detail/<int:pk>', InvoiceDetail.as_view(), name='detail'),
    path('edit/<int:pk>', InvoiceUpdate.as_view(), name='edit'),
    path('submit/<int:pk>', InvoiceUpdate.as_view(), {'process': 'submit'}, name='submit'),
    path('cancel/<int:pk>', InvoiceUpdate.as_view(), {'process': 'cancel'}, name='cancel'),
    path('create/', InvoiceCreate.as_view(), name='create'),

    path('add_line/', InvoiceLineCreate.as_view(), name='add_line'),
    path('delete_line/<int:pk>', InvoiceLineDelete.as_view(), name='delete_line'),
    path('edit_line/<int:pk>', InvoiceLineEdit.as_view(), name='edit_line'),

    path('create_stockentry/<int:invo_id>', CreateStockEntry.as_view(), name='create_stockentry'),
    path('list_stockentry/<int:invo_id>', ListStockEntry.as_view(), name='create_sotckentry'),
]
