# Generated by Django 4.0.6 on 2022-08-12 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productcategory_table_and_more'),
        ('orders', '0005_alter_shippingcost_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='product price')),
                ('quantity', models.IntegerField(default=1, verbose_name='product quantity')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products.product')),
            ],
            options={
                'db_table': 'Order Items',
                'ordering': ['-created_date'],
            },
        ),
    ]
