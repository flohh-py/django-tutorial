from django import forms
from django.forms import inlineformset_factory
from .models import Invoice, InvoiceLine


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


class InvoiceLineForm(forms.ModelForm):
    class Meta:
        model = InvoiceLine
        fields = '__all__'

InvoiceLineIF = inlineformset_factory(
    Invoice,
    InvoiceLine,
    fields= "__all__",
    form=InvoiceLineForm,
    extra= 1,
)
