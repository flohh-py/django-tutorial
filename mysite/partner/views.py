from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse 
from .models import Partner
from .forms import PartnerForm


class PartnerList(ListView):
    model = Partner
    template_name = 'partner/list.html'
    paginate_by = 10

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, *args, **kwargs):
        if self.is_ajax(request=self.request):
            ajax_val = self.request.GET['term']
            prod_obj = Partner.objects.all().filter(name__icontains=ajax_val)
            partners = list(prod_obj.values())
            return JsonResponse(partners, safe=False)

        return super(PartnerList, self).get(*args,**kwargs)


class PartnerCreate(CreateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'partner/create.html'
    success_url = reverse_lazy('partner:list')

