# Generated by Django 2.2.19 on 2022-06-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20220601_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='add_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
    ]
