# Generated by Django 4.0.6 on 2022-07-29 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productreview',
            options={'ordering': ['-created_date']},
        ),
    ]
