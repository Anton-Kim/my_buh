from django import forms


from .models import Item, Archive
# first_name = forms.CharField(label='Введите имя', initial='Лев')


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'purchase_unit_price', 'purchase_count', 'image')


class ItemSellForm(forms.ModelForm):
    class Meta:
        model = Archive
        fields = ('sell_unit_price', 'count', 'sell_date', 'comment')
