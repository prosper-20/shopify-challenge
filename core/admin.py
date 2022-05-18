from django.contrib import admin
from .models import Brand, Category, Product, Comment, Warehouse

# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)


class ProductAdmin(admin.ModelAdmin):
    model = Product


    list_display = ["name", "brand", "category", "seller", "status"]


admin.site.register(Product, ProductAdmin)



class CommentAdmin(admin.ModelAdmin):
    model = Comment

    list_display = ['name', "body", "date_added"]


admin.site.register(Comment, CommentAdmin)


class WarehouseAdmin(admin.ModelAdmin):
    model = Warehouse

    list_display = ['name','location', 'date_stored']

admin.site.register(Warehouse, WarehouseAdmin)
