from partner.models import Partner
from invoice.models import Invoice
from django.db import models
from main.models import NamingSeries as NS


PAY_TYPE = [
    ('pay', 'Pay'),
    ('receipt', 'Receipt'),
]
PAY_STATUS = [
    ('draft', 'Draft'),
    ('submitted', 'Submitted'),
    ('cancelled', 'Cancelled'),
]

class Payment(models.Model):
    code = models.CharField(max_length=12, null=True)
    date = models.DateField(null=True)
    partner = models.ForeignKey(Partner, related_name='payment_partner', on_delete=models.SET_NULL, null=True)
    type = models.CharField(choices=PAY_TYPE, default='', null=True, max_length=10)
    status = models.CharField(choices=PAY_STATUS, default='draft', null=True, max_length=10)
    total = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.code = NS.get_series(serie='PE')
        return super().save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse('paymenentry:detail', args=[self.id])


class PaymentLine(models.Model):
    item = models.ForeignKey(Invoice, related_name='pay_line_invo', on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey(Payment, related_name='pay_line_parant', on_delete=models.SET_NULL, null=True)
    type = models.CharField(choices=PAY_TYPE, default='', null=True, max_length=10)
    status = models.CharField(choices=PAY_STATUS, default='draft', null=True, max_length=10)
    total = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)
    allocated = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)
    outstanding = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)
