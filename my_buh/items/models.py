from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Item(models.Model):
    name = models.CharField(
        max_length=500,
        verbose_name='Название позиции',
        help_text='Введите название позиции'
    )
    add_date = models.DateField(
        verbose_name='Дата добавления',
        auto_now_add=True
    )
    purchase_price = models.PositiveIntegerField(
        verbose_name='Закупочная цена за единицу/штуку',
        help_text='Укажите закупочную цену за единицу/штуку'
    )
    sell_price = models.PositiveIntegerField(
        default=0,
        verbose_name='Цена продажи',
        help_text='Укажите цену продажи'
    )
    sell_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата продажи',
        help_text='Укажите дату продажи'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='purchased_items',
        verbose_name='Закупщик'
    )
    comment = models.TextField(
        max_length=10000,
        blank=True,
        null=True,
        verbose_name='Комментарий',
        help_text='Введите комментарий'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='',
        blank=True,
        help_text='Изображение позиции'
    )
    sold = models.BooleanField(
        verbose_name='Отметка о продаже',
        default=False
    )

    class Meta:
        ordering = ('-add_date', 'name')
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"

    def __str__(self):
        return self.name
