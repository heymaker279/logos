# Generated by Django 4.2.5 on 2024-01-04 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_productinfo_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinfo',
            name='image',
        ),
        migrations.RemoveField(
            model_name='productinfo',
            name='quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, help_text='Product photo', null=True, upload_to='main/images', verbose_name='Изображение товара'),
        ),
    ]
