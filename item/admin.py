from django.contrib import admin
from item.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = list_display
