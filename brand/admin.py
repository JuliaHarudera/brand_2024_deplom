from django.contrib import admin
from .models import Category, Product, Gallery, ContactUS
from django.utils.safestring import mark_safe


admin.site.register(ContactUS)
admin.site.register(Category)
admin.site.register(Gallery)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'order', 'category', 'brands', 'price', 'photo', 'sizes','photo_src_tag')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Product photo'

