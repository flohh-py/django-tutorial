from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse 
from .models import Product
from .forms import ProductForm


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    paginate_by = 8

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, *args, **kwargs):
        if self.is_ajax(request=self.request):
            ajax_val = self.request.GET['term']
            prod_obj = Product.objects.all().filter(code__icontains=ajax_val)
            products = list(prod_obj.values())
            return JsonResponse(products, safe=False)

        return super(ProductList, self).get(*args,**kwargs)


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

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, *args, **kwargs):
        if self.is_ajax(request=self.request):
            prod_data = Product.objects.filter(id=kwargs.get('pk')).values()[0]
            return JsonResponse(prod_data, safe=False)

        return super(ProductList, self).get(*args,**kwargs)


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('product:list')
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
