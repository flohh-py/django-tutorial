from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Payment, PaymentLine
from .forms import PaymentForm, PaymentLineForm
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

class PaymentList(ListView):
    model = Payment
    template_name = 'payment/list.html'
    paginate_by = 20


class PaymentDetail(DeleteView):
    model = Payment
    template_name = 'payment/detail.html'
    form_class = PaymentForm
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        lines = PaymentLine.objects.all().filter(parent=self.kwargs['pk'])
        context['lines'] = lines
        return context


class PaymentCreate(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment/create.html'

    def get_success_url(self):
        return reverse('payment:detail', kwargs={'pk':self.object.id})


class PaymentUpdate(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment/detail.html'
    fields = "__all__"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lines = PaymentLine.objects.all().filter(parent=self.kwargs['pk'])
        new_line = PaymentLineForm(initial={'parent':self.object})
        context['new_line'] = new_line
        context['lines'] = lines
        return context

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if kwargs.get('process') == 'submit':
            obj.submit_payment()
        
        if kwargs.get('process') == 'cancel':
            obj.cancel_payment()

        return redirect('payment:detail', pk=obj.id)


class PaymentLineCreate(CreateView):
    model = PaymentLine
    form_class = PaymentLineForm
    template_name = 'payment/add_line.html'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        return super(PaymentLineCreate, self).post(request, *args, **kwargs)

    def get_success_url(self):
        pk = self.request.POST['parent']
        return reverse('payment:detail', kwargs={'pk':pk})


class PaymentLineEdit(UpdateView):
    model = PaymentLine 
    form_class = PaymentLineForm
    template_name = 'payment/edit_line.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        line = PaymentLine.objects.get(pk=self.kwargs['pk'])
        return reverse('payment:detail', kwargs={'pk':line.parent.id})


class PaymentLineDelete(DeleteView):
    model = PaymentLine
    template_name = 'payment/delete_line.html'
    pk_url_kwarg = 'pk'

    def dispatch(self, request, *args, **kwargs):
        handler = getattr(self, 'delete')
        return handler(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('payment:detail', kwargs={'pk':self.object.parent.id})
