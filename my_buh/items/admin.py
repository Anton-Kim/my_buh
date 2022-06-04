from django.contrib import admin

from .models import Item, Archive


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_date', 'purchase_unit_price', 'count',
                    'sold_count', 'earnings', 'buyer', 'image')
    search_fields = ('name',)
    list_filter = ('name', 'add_date', 'earnings', 'buyer')
    empty_value_display = '-пусто-'


class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('item', 'sell_date', 'sell_unit_price', 'count',  'seller',
                    'comment')
    search_fields = ('item',)
    list_filter = ('item', 'sell_date', 'seller')
    empty_value_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
admin.site.register(Archive, ArchiveAdmin)
