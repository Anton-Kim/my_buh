# Generated by Django 2.2.19 on 2022-05-31 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20220531_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, help_text='Изображение позиции', upload_to='items/media/', verbose_name='Изображение'),
        ),
    ]
