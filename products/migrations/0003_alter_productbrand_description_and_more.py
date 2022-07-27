# Generated by Django 4.0.6 on 2022-07-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbrand',
            name='description',
            field=models.TextField(verbose_name='describe the brand'),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='name',
            field=models.CharField(max_length=254, verbose_name='brand name'),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='slug',
            field=models.SlugField(max_length=254, verbose_name='brand slug'),
        ),
    ]