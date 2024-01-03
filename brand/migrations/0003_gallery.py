# Generated by Django 5.0.1 on 2024-01-02 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_product_product_unique_order_per_each_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='product_images/')),
                ('is_visible', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]