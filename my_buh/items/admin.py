from django.contrib import admin

from .models import Item, Archive


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_date', 'purchase_unit_price',
                    'purchase_count', 'sold_count', 'earnings', 'owner',
                    'image')
    search_fields = ('name',)
    list_filter = ('name', 'add_date', 'earnings', 'owner')
    empty_value_display = '-пусто-'


class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'sell_date', 'sell_unit_price', 'count',
                    'seller', 'comment')
    search_fields = ('item_id',)
    list_filter = ('item_id', 'sell_date', 'seller')
    empty_value_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
admin.site.register(Archive, ArchiveAdmin)