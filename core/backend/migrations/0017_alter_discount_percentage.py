# Generated by Django 4.2.7 on 2023-11-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_variation_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='percentage',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]