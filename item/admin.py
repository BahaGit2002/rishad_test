from django.contrib import admin

from item.forms import OrderForm
from item.models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = list_display


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = list_display
    form = OrderForm




