# Generated by Django 4.0.6 on 2022-08-12 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productcategory_description_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productcategory',
            table='Product Categories',
        ),
        migrations.AlterModelTable(
            name='productreview',
            table='Product Reviews',
        ),
    ]
