from django.db import models
from product.models import Product
from main.models import NamingSeries as NS

ENTRY_STATUS = [
    ('draft', 'Draft'),
    ('submitted', 'Submitted'),
    ('cancelled', 'Cancelled'),
]
ENTRY_TYPE = [
    ('transfer', 'Transfer'),
    ('issue', 'Issue'),
    ('delivery', 'Delivery'),
    ('receipt', 'Receipt'),
]

class StockEntry(models.Model):
    code = models.CharField(max_length=10, null=True)
    date = models.DateField(null=True)
    type = models.CharField(choices=ENTRY_TYPE, default='', null=True, max_length=10)
    status = models.CharField(choices=ENTRY_STATUS, default='draft', null=True, max_length=10)
    total = models.FloatField(default=0.0)

    def __str__(self):
        return self.code

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            if self.type == 'transfer':
                self.code = NS.get_series(serie='TSTE')
            if self.type == 'issues':
                self.code = NS.get_series(serie='ISTE')
            if self.type == 'delivery':
                self.code = NS.get_series(serie='DSTE')
            if self.type == 'receipt':
                self.code = NS.get_series(serie='RSTE')
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ['code']


class StockEntryLine(models.Model):
    item = models.ForeignKey(Product, related_name='item', on_delete=models.CASCADE)
    parent = models.ForeignKey(StockEntry, related_name='parent', on_delete=models.CASCADE)
    qty = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
