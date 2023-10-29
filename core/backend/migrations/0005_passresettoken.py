# Generated by Django 4.2.6 on 2023-10-28 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassResetToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=5000)),
                ('validity', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pass_reset_tokens_set', to='backend.user')),
            ],
        ),
    ]
