# Generated by Django 2.2.19 on 2022-06-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_auto_20220601_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sell_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата продажи'),
        ),
    ]