from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
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
