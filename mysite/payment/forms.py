from django import forms
from .models import Payment, PaymentLine


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'date',
            'partner',
            'type',
        ]
        widgets = {
                'date': forms.DateInput(attrs={'class': 'form-control container col', 'type': 'date'}),
                'partner': forms.Select(attrs={'class': 'form-control'}),
                'type': forms.Select(attrs={'class': 'form-control'}),
                }


class PaymentLineForm(forms.ModelForm):
    class Meta:
        model = PaymentLine
        fields = [
            'item',
            'parent',
            'outstanding',
            'allocated',
        ]
        widgets = {
            'parent': forms.HiddenInput(),
            'outstanding': forms.HiddenInput(),
        }
