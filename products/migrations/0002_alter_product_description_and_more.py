# Generated by Django 4.0.6 on 2022-08-06 20:08

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=django_quill.fields.QuillField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=django_quill.fields.QuillField(),
        ),
    ]
