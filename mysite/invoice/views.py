from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.http import JsonResponse 
from .models import Invoice, InvoiceLine
from .forms import InvoiceForm, InvoiceLineIF, InvoiceLineForm
from stock.models import StockEntry, StockEntryLine
from stock.forms import StockEntryForm, StockEntryLineForm, StockEntryLineIF


class InvoiceList(ListView):
    model = Invoice
    template_name = 'invoice/list.html'
    paginate_by = 8

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, *args, **kwargs):
        if self.is_ajax(request=self.request):
            ajax_val = self.request.GET['term']
            invo_obj = Invoice.objects.all().filter(code__icontains=ajax_val)
            invoices = list(invo_obj.values())
            return JsonResponse(invoices, safe=False)

        return super(InvoiceList, self).get(*args, **kwargs)


class InvoiceDetail(DetailView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/detail.html'
    fields = "__all__"
    pk_url_kwarg = 'pk'

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, *args, **kwargs):
        if self.is_ajax(request=self.request):
            inv_data = Invoice.objects.filter(id=kwargs.get('pk')).values()[0]
            return JsonResponse(inv_data, safe=False)

        return super(InvoiceDetail, self).get(*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lines = InvoiceLine.objects.all().filter(parent=self.kwargs['pk'])
        new_line = InvoiceLineForm(initial={'parent':self.object})
        context['new_line'] = new_line
        context['lines'] = lines
        return context
        

class InvoiceCreate(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/create.html'
    success_url = reverse_lazy('invoice:list')

    def get_success_url(self):
        return reverse('invoice:detail', kwargs={'pk':self.object.id})


class InvoiceUpdate(UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/detail.html'
    fields = "__all__"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lines = InvoiceLine.objects.all().filter(parent=self.kwargs['pk'])
        new_line = InvoiceLineForm(initial={'parent':self.object})
        context['new_line'] = new_line
        context['lines'] = lines
        return context

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if kwargs.get('process') == 'submit':
            obj.submit_invoice(obj.id)
        
        if kwargs.get('process') == 'cancel':
            obj.cancel_invoice(obj.id)

        return redirect('invoice:detail', pk=obj.id)


class InvoiceLineCreate(CreateView):
    model = InvoiceLine
    form_class = InvoiceLineForm
    template_name = 'invoice/add_line.html'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        return super(InvoiceLineCreate, self).post(request, *args, **kwargs)

    def get_success_url(self):
        pk = self.request.POST['parent']
        return reverse('invoice:detail', kwargs={'pk':pk})


class InvoiceLineEdit(UpdateView):
    model = InvoiceLine
    form_class = InvoiceLineForm
    template_name = 'invoice/edit_line.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        line = InvoiceLine.objects.get(pk=self.kwargs['pk'])
        return reverse('invoice:detail', kwargs={'pk':line.parent.id})


class InvoiceLineDelete(DeleteView):
    model = InvoiceLine
    template_name = 'invoice/delete_line.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('invoice:detail', kwargs={'pk':self.object.parent.id})


class CreateStockEntry(CreateView):
    model = StockEntry
    form_class = StockEntryForm
    template_name = 'invoice/create_ste.html'
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # add val for template 
        context = super(CreateStockEntry, self).get_context_data(**kwargs)
        invo_obj = Invoice.objects.get(pk=self.kwargs['invo_id'])
        context['invo_obj'] = invo_obj

        context['form'] = StockEntryForm({
            'type': 'delivery' if invo_obj.type == 'sell' else 'receipt',
            'date': invo_obj.date
        })
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        self.object = form.save()
        self.object.parent = context['invo_obj']
        invoice_lines = InvoiceLine.objects.all().filter(parent=context['invo_obj'].id)
        for il in invoice_lines:
            if il.qty_stock > 0:
                line = StockEntryLineForm({
                    'invo_line': il,
                    'parent': self.object,
                    'item': il.item,
                    'qty': il.qty_stock,
                    'price': il.price,
                    })
                if line.is_valid():
                    line.save()

        return super(CreateStockEntry, self).form_valid(form)

    def get_success_url(self):
        return reverse('stock:detail', kwargs={'pk':self.object.id})


class ListStockEntry(ListView):
    model = StockEntry
    template_name = 'invoice/list_ste.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        invo_obj = Invoice.objects.get(pk=self.kwargs['invo_id'])
        ste_objs = StockEntry.objects.filter(parent=invo_obj.id)
        context['invoice'] = invo_obj
        context['object_list'] = ste_objs
        context['ste_count'] = ste_objs.count()
        return context
