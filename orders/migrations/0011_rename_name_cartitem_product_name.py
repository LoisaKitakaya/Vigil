# Generated by Django 4.0.6 on 2022-08-05 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_deliveryorder_item_alter_pickuporder_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='name',
            new_name='product_name',
        ),
    ]