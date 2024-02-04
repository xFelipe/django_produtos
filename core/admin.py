from django.contrib import admin

from core.models import Product

# Register your models here.
@admin.register(Product)    
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'image', 'slug', 'created_at', 'updated_at', 'active']
