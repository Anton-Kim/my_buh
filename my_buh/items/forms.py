from django import forms

from .models import Item, Archive, Comment


# first_name = forms.CharField(label='Введите имя', initial='Лев')


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'purchase_unit_price', 'count', 'image')


class ItemSellForm(forms.ModelForm):
    def __init__(self, form_count, *args, **kwargs):
        super(ItemSellForm, self).__init__(*args, **kwargs)
        if form_count:
            self.fields['count'] = forms.ChoiceField(
                choices=[(n, n) for n in range(1, form_count + 1)],
                label='Проданное количество'
            )
        else:
            del self.fields['sell_unit_price']
            del self.fields['count']
            del self.fields['sell_date']

    class Meta:
        model = Archive
        fields = ('sell_unit_price', 'count', 'sell_date', 'comment')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
