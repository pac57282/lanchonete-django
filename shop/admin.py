from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}   #especificar os campos os quais o valor é automaticamente definido com base no valor de outros campos

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']   #permite que dite várias linhas ao mesmo tempo
    prepopulated_fields = {'slug': ('name',)}   #especificar os campos os quais o valor é automaticamente definido com base no valor de outros campos

