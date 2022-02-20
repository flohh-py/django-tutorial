from django import forms
from .models import StockEntry, StockEntryLine


class StockEntryForm(forms.ModelForm):
    class Meta:
        model = StockEntry
        fields = [
                'date',
                'type',
                ]
        widgets = {
                'date': forms.DateInput(attrs={'class': 'form-control container col', 'type': 'date'}),
                'type': forms.Select(attrs={'class': 'form-control'}),
                }


class StockEntryLineForm(forms.ModelForm):
    class Meta:
        model = StockEntryLine
        fields = [
            'parent',
            'item',
            'qty',
            'price'
        ]
        widgets = {
            'aprent': forms.HiddenInput(),
        }

