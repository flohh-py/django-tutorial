from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    paginate_by = 10


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('product:list')


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/update.html'
    # fields = "__all__"
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('product:list')


class ProductDetail(DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'product/detail.html'
    fields = "__all__"
    pk_url_kwarg = 'pk'


# class ProductCreate(View):
#     template = 'product/product_create.html'
#     def get(self, request, pk=None):
#         if pk:
#             print(pk)
#             products = Product.objects.get(id=pk)
#             prod_form = ProductForm(instance=products)
#         else:
#             prod_form = ProductForm()

#         context = {
#             'products': prod_form
#         }
#         return render(request=request, template_name=self.template, context=context)

#     def post(self, request, pk=None):
#         prod_form = ProductForm(request.POST)
#         if prod_form.is_valid():
#             prod_form.save()

#         return redirect('products_list')
        

# class ProductUpdate(View):
#     def post(self, request, pk=None):
#         if pk:
#             products = Product.objects.get(id=pk)
#             prod_form = ProductForm(instance=products)
#             if prod_form.is_valid():
#                 prod_form.save()
#                 return redirect('products_list')
