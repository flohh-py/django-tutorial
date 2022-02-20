from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import StockEntry, StockEntryLine
from .forms import StockEntryForm, StockEntryLineForm


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
    success_url = reverse_lazy('stock:list')


class StockEntryLineAdd(CreateView):
    model = StockEntryLine
    form_class = StockEntryLineForm
    template_name = 'stock/detail.html'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('stock:detail', kwargs={'pk':pk})
