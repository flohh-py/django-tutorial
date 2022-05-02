from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .models import StockEntry, StockEntryLine
from .forms import StockEntryForm, StockEntryLineForm, StockEntryLineIF
from main.views import BaseView


class StockEntryList(BaseView, ListView):
    model = StockEntry
    template_name = 'stock/list.html'
    paginate_by = 8
    permission_required = 'stockentry.view_stockentry'


class StockEntryDetail(BaseView, DetailView):
    model = StockEntry
    form_class = StockEntryForm
    template_name = 'stock/detail.html'
    fields = "__all__"
    pk_url_kwarg = 'pk'
    permission_required = 'stockentry.view_stockentry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lines = StockEntryLine.objects.all().filter(parent=self.kwargs['pk'])
        new_line = StockEntryLineForm(initial={'parent':self.object})
        context['new_line'] = new_line
        context['lines'] = lines
        return context
        

class StockEntryCreate(BaseView, CreateView):
    model = StockEntry
    form_class = StockEntryForm
    template_name = 'stock/create.html'
    permission_required = 'stockentry.add_stockentry'

    def get_success_url(self):
        return reverse('stock:detail', kwargs={'pk':self.object.id})


class StockEntryUpdate(BaseView, UpdateView):
    model = StockEntry
    form_class = StockEntryForm
    formset_class = StockEntryLineIF
    template_name = 'stock/detail.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('stock:detail')
    permission_required = 'stockentry.change_stockentry'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     lines = StockEntryLine.objects.all().filter(parent=self.kwargs['pk'])
    #     new_line = StockEntryLineForm(initial={'parent':self.object})
    #     context['new_line'] = new_line
    #     context['lines'] = lines
    #     return context

    # def get_success_url(self):
    #     pk = self.kwargs['pk']
    #     return reverse('stock:detail', kwargs={'pk':pk})

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if kwargs.get('process') == 'submit':
            obj.submit_stock_entry(obj.id)
        
        if kwargs.get('process') == 'cancel':
            obj.cancel_stock_entry(obj.id)

        return redirect('stock:detail', pk=obj.id)

class StockEntryLineCreate(BaseView, CreateView):
    model = StockEntryLine
    form_class = StockEntryLineForm
    template_name = 'stock/add_line.html'
    pk_url_kwarg = 'pk'
    permission_required = 'stockentryline.add_stockentryline'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['parent'] = self.kwargs['pk']
    #     return context

    def get_success_url(self):
        # pk = self.kwargs['pk']
        # parent = StockEntry.objects.get(pk=self.kwargs['pk'])
        parent_id = self.request.POST['parent']
        return reverse('stock:detail', kwargs={'pk':parent_id})


class StockEntryLineEdit(BaseView, UpdateView):
    model = StockEntryLine
    form_class = StockEntryLineForm
    template_name = 'stock/edit_line.html'
    pk_url_kwarg = 'pk'
    permission_required = 'stockentryline.change_stockentryline'

    def get_success_url(self):
        line = StockEntryLine.objects.get(pk=self.kwargs['pk'])
        return reverse('stock:detail', kwargs={'pk':line.parent.id})


class StockEntryLineDelete(BaseView, DeleteView):
    model = StockEntryLine
    template_name = 'stock/delete_line.html'
    pk_url_kwarg = 'pk'
    permission_required = 'stockentryline.delete_stockentryline'

    def get_success_url(self):
        return reverse('stock:detail', kwargs={'pk':self.object.parent.id})
