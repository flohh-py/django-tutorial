from django import forms
from django.forms import inlineformset_factory
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
            'parent': forms.HiddenInput(),
        }

StockEntryLineIF= inlineformset_factory(
    StockEntry,
    StockEntryLine,
    fields= "__all__",
    form=StockEntryLineForm,
    extra= 0,
)
