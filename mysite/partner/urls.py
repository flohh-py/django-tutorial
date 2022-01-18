from django.urls import path
from .views import *

app_name = "partner"
urlpatterns = [
    path('', PartnerList.as_view(), name='list'),
    path('create/', PartnerCreate.as_view(), name='create'),
    # path('detail/<int:pk>', PartnerDetail.as_view(), name='detail'),
    path('edit/<int:pk>', PartnerUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', PartnerDelete.as_view(), name='delete'),
]
