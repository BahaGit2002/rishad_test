from django.db import models


class CurrencyChoices(models.TextChoices):
    usd = 'USD'
    gbp = 'GBP'
