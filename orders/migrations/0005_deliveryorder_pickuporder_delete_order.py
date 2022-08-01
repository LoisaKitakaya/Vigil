# Generated by Django 4.0.6 on 2022-07-29 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_alter_cartitem_options_alter_order_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=254, verbose_name='city of residence')),
                ('address', models.CharField(max_length=254, verbose_name='address 1')),
                ('phone_one', models.CharField(max_length=254, verbose_name='primary phone')),
                ('phone_two', models.CharField(max_length=254, verbose_name='secondary phone')),
                ('order_uic', models.CharField(max_length=254, verbose_name='order unique identification code')),
                ('total', models.FloatField(default=0, verbose_name='total payable')),
                ('approved', models.BooleanField(default=False, verbose_name='approved for shipping')),
                ('fulfilled', models.BooleanField(default=False, verbose_name='has been fulfilled')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('item', models.ManyToManyField(to='orders.cartitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner of order')),
            ],
            options={
                'db_table': 'Delivery Order Table',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='PickupOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_identification', models.CharField(max_length=254, verbose_name='personal identification')),
                ('phone_one', models.CharField(max_length=254, verbose_name='primary phone')),
                ('phone_two', models.CharField(max_length=254, verbose_name='secondary phone')),
                ('order_uic', models.CharField(max_length=254, verbose_name='order unique identification code')),
                ('total', models.FloatField(default=0, verbose_name='total payable')),
                ('approved', models.BooleanField(default=False, verbose_name='approved for shipping')),
                ('fulfilled', models.BooleanField(default=False, verbose_name='has been fulfilled')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('item', models.ManyToManyField(to='orders.cartitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner of order')),
            ],
            options={
                'db_table': 'Pickup Order Table',
                'ordering': ['-created_date'],
            },
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]