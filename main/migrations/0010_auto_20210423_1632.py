# Generated by Django 3.1.7 on 2021-04-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210423_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/teachers', verbose_name='Добавить фото'),
        ),
    ]
