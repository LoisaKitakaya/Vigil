# Generated by Django 4.0.6 on 2022-07-26 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='full_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=254, verbose_name='product full name'),
            preserve_default=False,
        ),
    ]