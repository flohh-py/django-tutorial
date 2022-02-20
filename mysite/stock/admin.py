from django.contrib import admin
from .models import StockEntry, StockEntryLine


admin.site.register(StockEntry)
admin.site.register(StockEntryLine)
