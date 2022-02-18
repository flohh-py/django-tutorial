from django import forms
from django.forms import inlineformset_factory
from .models import Invoice, InvoiceLine
from product.models import Product


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
                'code',
                'date',
                'partner',
                'type',
                'total',
                ]
        widgets = {
                'code': forms.TextInput(attrs={'class': 'form-control'}),
                'date': forms.DateInput(attrs={'class': 'form-control container col', 'type': 'date'}),
                'partner': forms.Select(attrs={'class': 'form-control'}),
                'type': forms.Select(attrs={'class': 'form-control'}),
                'total': forms.TextInput(attrs={'class': 'form-control'}),
                }


class InvoiceLineForm(forms.ModelForm):
    class Meta:
        model = InvoiceLine
        fields = [
            'invoice',
            'product',
            'qty',
            'price'
        ]
        widgets = {
            'invoice': forms.HiddenInput(),
        }


InvoiceLineIF = inlineformset_factory(
    Invoice,
    InvoiceLine,
    fields= "__all__",
    form=InvoiceLineForm,
    extra= 1,
)
