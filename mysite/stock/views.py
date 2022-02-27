from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .models import StockEntry, StockEntryLine
from .forms import StockEntryForm, StockEntryLineForm, StockEntryLineIF


class StockEntryList(ListView):
    model = StockEntry
    template_name = 'stock/list.html'
    paginate_by = 8


class StockEntryDetail(DetailView):
    model = StockEntry
    form_class = StockEntryForm
    template_name = 'stock/detail.html'
    fields = "__all__"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lines = StockEntryLine.objects.all().filter(parent=self.kwargs['pk'])
        new_line = StockEntryLineForm(initial={'parent':self.object})
        context['new_line'] = new_line
        context['lines'] = lines
        return context
        

class StockEntryCreate(CreateView):
    model = StockEntry
    form_class = StockEntryForm
    template_name = 'stock/create.html'

    def get_success_url(self):
        return reverse('stock:detail', kwargs={'pk':self.object.id})


class StockEntryUpdate(UpdateView):
    model = StockEntry
    form_class = StockEntryForm
    formset_class = StockEntryLineIF
    template_name = 'stock/detail.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('stock:detail')

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

class StockEntryLineCreate(CreateView):
    model = StockEntryLine
    form_class = StockEntryLineForm
    template_name = 'stock/add_line.html'
    pk_url_kwarg = 'pk'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['parent'] = self.kwargs['pk']
    #     return context

    def get_success_url(self):
        # pk = self.kwargs['pk']
        # parent = StockEntry.objects.get(pk=self.kwargs['pk'])
        parent_id = self.request.POST['parent']
        return reverse('stock:detail', kwargs={'pk':parent_id})

class StockEntryLineEdit(UpdateView):
    model = StockEntryLine
    form_class = StockEntryLineForm
    template_name = 'stock/edit_line.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        line = StockEntryLine.objects.get(pk=self.kwargs['pk'])
        return reverse('stock:detail', kwargs={'pk':line.parent.id})

class StockEntryLineDelete(DeleteView):
    model = StockEntryLine
    template_name = 'stock/delete_line.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('stock:detail', kwargs={'pk':self.object.parent.id})
