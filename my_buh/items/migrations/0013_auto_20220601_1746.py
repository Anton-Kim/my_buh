# Generated by Django 2.2.19 on 2022-06-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_auto_20220601_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='selling_price',
            field=models.PositiveIntegerField(blank=True, help_text='Укажите цену продажи', null=True, verbose_name='Цена продажи'),
        ),
    ]