from django.db import models
from django.core.validators import RegexValidator
"""
модели и из преднозначение к каждой модели нужно добавить имя=name место=order и описание=description
следом по желанию добавить отображения сезоного товара или просто его отобразить=is_visible и фото вещи=photo

первая катерогия = категория товаров для сайта буд-то вещи или инные товары 

следуящая продукты = под катерогия Категорий  в нее надо внести сами вещи или товары 

под канец галерея = в нее нужно ввести фото товара для презентаций 

"""

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('order', )

    def __iter__(self):
        products = self.products.filter(is_visible=True)
        for product in products:
            yield product

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brands = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='product_images/', blank=True)
    sizes = models.CharField(max_length=50, help_text='Comma-separated list of available sizes',blank=True)
    quantity_available = models.PositiveIntegerField()
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('order',)
        constraints = [
            models.UniqueConstraint(fields=['order', 'category'], name='unique_order_per_each_category'),
        ]
        unique_together = ['id', 'slug']


class Gallery(models.Model):
    photo = models.ImageField(upload_to='product_images/')
    is_visible = models.BooleanField(default=True)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name}"


class ContactUS(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?\d{7,12}$', message='Phone number should be in format: +380')
    phone = models.CharField(validators=[phone_regex, ], max_length=20)
    message = models.TextField(max_length=500, blank=True)

    is_precessed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        ordering = ('-created_at',)




