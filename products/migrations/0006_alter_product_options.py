# Generated by Django 4.0.6 on 2022-07-28 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_date']},
        ),
    ]