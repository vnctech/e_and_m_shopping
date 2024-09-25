from django.contrib import admin
from .models import Category, Subcategory, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category'] 

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'subcategory', 'price']  

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
