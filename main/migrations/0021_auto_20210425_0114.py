# Generated by Django 3.1.7 on 2021-04-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210425_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersdetail',
            name='edu',
            field=models.CharField(max_length=500, verbose_name='Образоание'),
        ),
    ]
