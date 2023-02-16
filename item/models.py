from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=11, decimal_places=2)

    class Meta:
        verbose_name = ' Элемент'
        verbose_name_plural = 'Элементы'

    def __str__(self):
        return f'{self.name}'
