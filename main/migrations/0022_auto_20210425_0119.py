# Generated by Django 3.1.7 on 2021-04-24 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210425_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersdetail',
            name='certificates',
            field=models.CharField(max_length=500, verbose_name='Сертификаты'),
        ),
    ]