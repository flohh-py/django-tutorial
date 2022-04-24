from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse 
from .models import Partner
from .forms import PartnerForm
from main.views import BaseView

class PartnerList(BaseView, ListView):
    model = Partner
    template_name = 'partner/list.html'
    paginate_by = 10
    permission_required = 'partner.view_partner'

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def get(self, *args, **kwargs):
        if self.is_ajax(request=self.request):
            ajax_val = self.request.GET['term']
            ajax_filter = ''
            if self.request.GET['type'] in ('sell', 'receipt'):
                ajax_filter = 'customer'
            if self.request.GET['type'] in ('purchase','pay'):
                ajax_filter = 'supplier' 
            part_obj = Partner.objects.all().filter(
                name__icontains=ajax_val,
                type=ajax_filter
            )
            partners = list(part_obj.values())
            return JsonResponse(partners, safe=False)

        return super(PartnerList, self).get(*args,**kwargs)


class PartnerCreate(BaseView, CreateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'partner/create.html'
    success_url = reverse_lazy('partner:list')
    permission_required = 'partner.add_partner'


class PartnerUpdate(BaseView, UpdateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'partner/update.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('partner:list')
    permission_required = 'partner.change_partner'


class PartnerDelete(BaseView, DeleteView):
    model = Partner
    template_name = 'partner/delete.html'
    success_url = reverse_lazy('partner:list')
    pk_url_kwarg = 'pk'
    permission_required = 'partner.delete_partner'
