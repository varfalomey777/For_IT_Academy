# Generated by Django 4.1.7 on 2023-02-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Описание авто '),
        ),
        migrations.AlterField(
            model_name='post',
            name='cost',
            field=models.IntegerField(verbose_name='Стоимость авто '),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название авто '),
        ),
        migrations.AlterField(
            model_name='post',
            name='name_user',
            field=models.CharField(max_length=20, verbose_name='Ваше имя '),
        ),
        migrations.AlterField(
            model_name='post',
            name='number_user',
            field=models.IntegerField(verbose_name='Контактный телефон '),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='all_photos/%Y/%m/%d/', verbose_name='Фотография авто '),
        ),
        migrations.AlterField(
            model_name='post',
            name='year',
            field=models.IntegerField(verbose_name='Год выпуска '),
        ),
    ]
