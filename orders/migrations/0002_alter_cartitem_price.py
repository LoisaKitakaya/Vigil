# Generated by Django 4.0.6 on 2022-07-27 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.FloatField(default=0, verbose_name='product price'),
        ),
    ]
