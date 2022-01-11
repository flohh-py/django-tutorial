from django.db import models
from django.urls import reverse
from product.models import Product


class Invoice(models.Model):
    code = models.CharField(max_length=10, null=True)
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
