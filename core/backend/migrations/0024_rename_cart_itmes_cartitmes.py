# Generated by Django 4.2.6 on 2023-12-08 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('backend', '0023_product_is_featured_product_is_recommended_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart_itmes',
            new_name='CartItmes',
        ),
    ]
