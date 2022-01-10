from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
                'code',
                'total',
                ]
        widgets = {
                'code': forms.TextInput(attrs={'class': 'form-control'}),
                'total': forms.TextInput(attrs={'class': 'form-control'}),
                }
