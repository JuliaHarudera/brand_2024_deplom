# Generated by Django 5.0.1 on 2024-01-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0005_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='message',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]