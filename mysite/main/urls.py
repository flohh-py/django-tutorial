from django.urls import path, include
from .views import MainView, MainLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', MainLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='main_url'), name='logout'),
    path('', MainView.as_view(), name='main_url'),
]
