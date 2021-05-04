# Generated by Django 3.1.7 on 2021-04-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Добавить фото')),
                ('name', models.CharField(max_length=70, verbose_name='Ф.И.О')),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Добавить фото'),
        ),
    ]