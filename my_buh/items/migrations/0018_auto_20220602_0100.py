# Generated by Django 2.2.19 on 2022-06-01 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_auto_20220602_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archive',
            name='item_id',
        ),
        migrations.AddField(
            model_name='archive',
            name='item',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='sold_items', to='items.Item', verbose_name='Проданные позиции'),
            preserve_default=False,
        ),
    ]