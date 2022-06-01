# Generated by Django 2.2.19 on 2022-06-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0016_auto_20220601_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archive',
            options={'ordering': ('-sell_date', 'item_id'), 'verbose_name': 'Проданная позиция', 'verbose_name_plural': 'Проданные позиции'},
        ),
        migrations.RemoveField(
            model_name='archive',
            name='item',
        ),
        migrations.AddField(
            model_name='archive',
            name='item_id',
            field=models.IntegerField(default=0, verbose_name='ID продаваемой позиции'),
        ),
    ]