from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_date', 'purchase_price', 'sell_price',
                    'sell_date', 'owner', 'comment', 'sold')
    search_fields = ('name', 'comment')
    list_filter = ('name', 'add_date')
    empty_value_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
