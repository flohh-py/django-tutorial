from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Product
from .forms import ProductForm


class ProductList(View):
    template = 'product/product.html'

    def get(self, request):
        products = list(Product.objects.values())

        context = {
            'products': products,
        }

        return render(request=request, template_name=self.template, context=context)

class ProductCreate(View):
    template = 'product/product_create.html'
    def get(self, request, pk=None):
        if pk:
            print(pk)
            products = Product.objects.get(id=pk)
            prod_form = ProductForm(instance=products)
        else:
            prod_form = ProductForm()

        context = {
            'products': prod_form
        }
        return render(request=request, template_name=self.template, context=context)

    def post(self, request, pk=None):
        prod_form = ProductForm(request.POST)
        if prod_form.is_valid():
            prod_form.save()

        return redirect('products_list')
        

class ProductUpdate(View):
    def post(self, request, pk=None):
        if pk:
            products = Product.objects.get(id=pk)
            prod_form = ProductForm(instance=products)
            if prod_form.is_valid():
                prod_form.save()
                return redirect('products_list')
