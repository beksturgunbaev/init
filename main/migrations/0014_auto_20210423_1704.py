# Generated by Django 3.1.7 on 2021-04-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210423_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news', verbose_name='Добавить фото'),
        ),
    ]
