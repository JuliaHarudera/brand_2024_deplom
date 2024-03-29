# Generated by Django 5.0.1 on 2024-01-19 21:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0004_alter_product_sizes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Phone number should be in format: +380', regex='^\\+?\\d{7,12}$')])),
                ('is_precessed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
