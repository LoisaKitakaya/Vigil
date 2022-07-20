# Generated by Django 4.0.6 on 2022-07-20 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='category name')),
                ('slug', models.SlugField(max_length=254, verbose_name='category slug')),
                ('description', models.TextField(verbose_name='describe the category')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Products Category',
                'ordering': ['created_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='quantity of product')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Products Inventory',
                'ordering': ['created_date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='product name')),
                ('slug', models.SlugField(max_length=254, verbose_name='product slug')),
                ('price', models.IntegerField(default=0, verbose_name='product price')),
                ('thumbnail', models.URLField(max_length=254, verbose_name='product thumbnail')),
                ('description', models.TextField(verbose_name='describe the product')),
                ('slide_one', models.URLField(max_length=254, verbose_name='product slide 1')),
                ('slide_two', models.URLField(max_length=254, verbose_name='product slide 2')),
                ('slide_three', models.URLField(max_length=254, verbose_name='product slide 3')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory')),
                ('product_inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productinventory')),
            ],
            options={
                'db_table': 'Products Table',
                'ordering': ['created_date'],
            },
        ),
    ]