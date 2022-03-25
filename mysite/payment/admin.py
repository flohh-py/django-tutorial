from django.contrib import admin
from .models import Payment, PaymentLine


admin.site.register(Payment)
admin.site.register(PaymentLine)
