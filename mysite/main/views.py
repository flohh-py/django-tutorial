from django.shortcuts import render
from django.views.generic import View
from .models import Main


class MainView(View):
    def get(self, request):
        titles = list(Main.objects.values())

        return render(request, 'main/main.html')
