# Generated by Django 3.1.7 on 2021-04-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210423_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='teachers', verbose_name='Добавить фото'),
        ),
        migrations.AlterField(
            model_name='teachersdetail',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='teachers', verbose_name='Добавить фото'),
        ),
    ]
