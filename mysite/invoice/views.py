from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Invoice, InvoiceLine
from .forms import InvoiceForm, InvoiceLineIF


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
        

class InvoiceCreate(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/create.html'
    success_url = reverse_lazy('invoice:list')

    def get_context_data(self, **kwargs):
        context = super(InvoiceCreate, self).get_context_data(**kwargs)

        if self.request.POST:
            context['lines'] = InvoiceLineIF(self.request.POST)
                
        else:
            context['lines'] = InvoiceLineIF()

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        lines = context['lines']
        if lines.is_valid():
            self.object = form.save()
            lines.instance = self.object
            lines.save()

        return super(InvoiceCreate, self).form_invalid(form)
