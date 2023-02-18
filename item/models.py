from django.db import models
from item.choices import CurrencyChoices


class Item(models.Model):
    name = models.CharField( max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    currency = models.CharField(max_length=255, choices=CurrencyChoices.choices)

    class Meta:
        verbose_name = ' Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    items = models.ManyToManyField('Item', related_name='orders', verbose_name='Элементы')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.id}'
