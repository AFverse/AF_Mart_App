# Generated by Django 4.2.6 on 2023-12-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]