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
                'date': forms.SelectDateWidget(attrs={'class': 'form-control container col'}),
                'partner': forms.Select(attrs={'class': 'form-control'}),
                'type': forms.Select(attrs={'class': 'form-control'}),
                'total': forms.TextInput(attrs={'class': 'form-control'}),
                }


class InvoiceLineForm(forms.ModelForm):
    class Meta:
        model = InvoiceLine
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['product'].queryset = Product.objects.none()

    #     if 'product' in self.data:
    #         self.fields['product'].queryset = Product.objects.all()


InvoiceLineIF = inlineformset_factory(
    Invoice,
    InvoiceLine,
    fields= "__all__",
    form=InvoiceLineForm,
    extra= 1,
)
