# Generated by Django 3.2 on 2021-10-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20211007_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='items_json',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(max_length=111),
        ),
    ]
