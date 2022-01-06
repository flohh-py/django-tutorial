from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
                'code',
                'descrip',
                'price',
                'purchase',
                'qty',
                ]
        widgets = {
                'code': forms.TextInput(attrs={'class': 'form-control'}),
                'descrip': forms.TextInput(attrs={'class': 'form-control'}),
                'price': forms.TextInput(attrs={'class': 'form-control'}),
                'purchase': forms.TextInput(attrs={'class': 'form-control'}),
                'qty': forms.TextInput(attrs={'class': 'form-control'}),
                }
