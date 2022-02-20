from django.db import models
from django.urls import reverse
from product.models import Product
from partner.models import Partner
from main.models import NamingSeries as NS


INVO_TYPE = [
    ('sell', 'Sell'),
    ('purchase', 'Purchase'),
]
INVO_STATUS = [
    ('draft', 'Draft'),
    ('submitted', 'Submitted'),
    ('cancelled', 'Cancelled'),
]

class Invoice(models.Model):
    code = models.CharField(max_length=10, null=True)
    date = models.DateField(null=True)
    partner = models.ForeignKey(Partner, related_name='partner', on_delete=models.CASCADE, null=True)
    type = models.CharField(choices=INVO_TYPE, default='', null=True, max_length=10)
    status = models.CharField(choices=INVO_STATUS, default='draft', null=True, max_length=10)
    total = models.FloatField(default=0.0)

    def __str__(self):
        return self.code

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            if self.type == 'purchase':
                self.code = NS.get_series(serie='PINV')
            if self.type == 'sell':
                self.code = NS.get_series(serie='SINV')
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ['code']


class InvoiceLine(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, related_name='invoice', on_delete=models.CASCADE)
    qty = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
