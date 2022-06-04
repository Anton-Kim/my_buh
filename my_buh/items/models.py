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
    purchase_unit_price = models.PositiveIntegerField(
        verbose_name='Закупочная цена за 1 шт.',
        help_text='Укажите закупочную цену за 1 шт.'
    )
    count = models.PositiveIntegerField(
        verbose_name='Купленное количество',
        help_text='Укажите купленное количество'
    )
    sold_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Проданное количество'
    )
    earnings = models.IntegerField(
        default=0,
        verbose_name='Выручка'
    )
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='purchased_items',
        verbose_name='Закупщик'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='',
        blank=True,
        help_text='Изображение позиции'
    )
    # sold = models.BooleanField(
    #     verbose_name='Отметка о продаже',
    #     default=False
    # )

    class Meta:
        ordering = ('-add_date', 'name')
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"

    def __str__(self):
        return self.name


class Archive(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='sold_items',
        verbose_name='Проданные позиции'
    )
    sell_date = models.DateField(
        verbose_name='Дата продажи',
        help_text='Укажите дату продажи'
    )
    sell_unit_price = models.PositiveIntegerField(
        verbose_name='Цена продажи за 1 шт.',
        help_text='Укажите цену продажи за 1 шт.'
    )
    count = models.PositiveIntegerField(
        verbose_name='Проданное количество',
        help_text='Укажите проданное количество'
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sold_items',
        verbose_name='Продавец'
    )
    comment = models.TextField(
        max_length=10000,
        blank=True,
        null=True,
        verbose_name='Комментарий',
        help_text='Необязательный комментарий'
    )

    class Meta:
        ordering = ('-sell_date', 'item_id')
        verbose_name = "Проданная позиция"
        verbose_name_plural = "Проданные позиции"

    def __str__(self):
        return self.item.name


class Comment(models.Model):
    text = models.TextField(
        max_length=10000,
        verbose_name='Текст комментария',
        help_text='Введите текст комментария'
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text[:15]
