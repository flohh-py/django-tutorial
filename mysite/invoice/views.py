from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import Invoice, InvoiceLine
from .forms import InvoiceForm, InvoiceLineIF, InvoiceLineForm


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
        new_line = InvoiceLineForm(initial={'invoice':self.object})
        context['new_line'] = new_line
        context['lines'] = lines
        return context
        

class InvoiceCreate(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/create.html'
    success_url = reverse_lazy('invoice:list')


class InvoiceLineAdd(CreateView):
    model = InvoiceLine
    form_class = InvoiceLineForm
    template_name = 'invoice/detail.html'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        # invoice = Invoice.objects.get(pk=self.kwargs['pk'])
        return super(InvoiceLineAdd, self).post(request, *args, **kwargs)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('invoice:detail', kwargs={'pk':pk})
