# Generated by Django 4.2.7 on 2023-11-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_remove_release_time_release_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='year',
            field=models.IntegerField(verbose_name='Укажите дату релиза'),
        ),
    ]
