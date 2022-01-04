from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Product


class ProductView(View):
    template = 'product/product.html'

    def get(self, request, id=None):
        if id:
            product_pk = list(Product.objects.values().filter(pk=id))
        else:
            products = list(Product.objects.values())

        return render(request, self.template)

    def post(self, request, id=None):
        if id:
            product_pk = list(Product.objects.values().filter(pk=id))

        return redirect('product_list')
        
