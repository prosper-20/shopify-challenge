from django.contrib import admin
from .models import Brand, Category, Product

# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)


class ProductAdmin(admin.ModelAdmin):
    model = Product


    list_display = ["name", "brand", "category", "seller", "status"]


admin.site.register(Product, ProductAdmin)
