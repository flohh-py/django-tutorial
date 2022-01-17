from django.db import models
from django.urls import reverse
from product.models import Product

INVO_TYPE = [
    ('sell', 'Sell'),
    ('purchase', 'Purchase'),
]

class Invoice(models.Model):
    code = models.CharField(max_length=10, null=True)
    date = models.DateField(null=True)
    type = models.CharField(choices=INVO_TYPE, default='sell', null=True, max_length=10)
    total = models.FloatField(default=0.0)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ['code']


class InvoiceLine(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, related_name='invoice', on_delete=models.CASCADE)
    qty = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
