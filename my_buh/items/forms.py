from django import forms


from .models import Item
# first_name = forms.CharField(label='Введите имя', initial='Лев')


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'purchase_price', 'image')


class ItemSellForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('sell_price', 'sell_date', 'comment')
