from django import forms
from django.core.exceptions import ValidationError

from item.models import Order, Item
from item.choices import CurrencyChoices


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('items',)

    def clean(self):
        cleaned_data = super().clean()
        items_usd = Item.objects.filter(id__in=self['items'].value(), currency=CurrencyChoices.usd)
        items_gbp = Item.objects.filter(id__in=self['items'].value(), currency=CurrencyChoices.gbp)
        if items_gbp and items_usd:
            raise ValidationError("You cannot select two items with different currencies")
        return cleaned_data



