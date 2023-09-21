from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug' : ['product_name']}
    list_display = ['product_name', 'slug' , 'stock', 'category']
 
admin.site.register(Product, ProductAdmin)
