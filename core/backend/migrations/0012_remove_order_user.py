# Generated by Django 4.2.7 on 2023-11-22 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_delete_otp_remove_token_user_alter_cart_itmes_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]