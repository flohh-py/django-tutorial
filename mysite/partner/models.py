from django.db import models
from django.urls import reverse

PARTNER_TYPE = [
    ('supplier', 'Supplier'),
    ('customer', 'Customer'),
]

class Partner(models.Model):
    name = models.CharField(max_length=50, null=True)
    type = models.CharField(choices=PARTNER_TYPE, default='customer', null=True, max_length=10)
    address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('partner:detail', args=[self.id])
