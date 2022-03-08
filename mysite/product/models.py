from django.db import models
from django.urls import reverse

PROD_TYPE = [
    ('stockable', 'Stockable'),
    ('service', 'Service'),
]

class Product(models.Model):
    code = models.CharField(max_length=50, null=True)
    type = models.CharField(choices=PROD_TYPE, default='stockable', null=True, max_length=10)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)
    cost = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)
    descrip = models.CharField(max_length=120)
    qty = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.type == 'service':
            self.qty = 1.0
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.code
    
    def get_absolute_url(self):
        # return 'prduct:list', (), {'slug': self.slug}
        return reverse('product:detail', args=[self.id])

    @classmethod
    def update_product_stock(cls, line=None, type=None):
        if line and type:
            prod = cls.objects.get(pk=line.item.id)
            old_cost = prod.cost * prod.qty
            new_cost = line.price * line.qty

            if type == 'in':
                prod.cost = ((old_cost + new_cost) / (prod.qty + line.qty))
                prod.qty = prod.qty + line.qty

            if type == 'out':
                prod.qty = prod.qty - line.qty

            prod.save()
            return True

    class Meta:
        ordering = ['code']
