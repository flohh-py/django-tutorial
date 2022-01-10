from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Invoice, InvoiceLine
from .forms import InvoiceForm


class InvoiceList(ListView):
    model = Invoice
    template_name = 'invoice/list.html'
    paginate_by = 20


class InvoiceDetail(DetailView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/detail.html'
    fields = "__all__"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            lines = InvoiceLine.objects.all().filter(invoice=self.kwargs['pk'])
            context['lines'] = lines
            return context
        
