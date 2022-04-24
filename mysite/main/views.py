from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class BaseView(LoginRequiredMixin, PermissionRequiredMixin):
    pass


class MainLoginView(LoginView):
    template_name = 'main/mainlogin.html'
    fields = '__all__'
    redirect_authenticated_user = True
    permission_required = None

    def get_redirect_url(self):
        return reverse_lazy('main_url')

class MainView(LoginRequiredMixin, View):
    def get(self, request):

        return render(request, 'main/main.html')
