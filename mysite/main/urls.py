from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main_url'),
    path('product/', include('product.urls'))
]
