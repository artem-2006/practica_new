from django.contrib import admin

from django.contrib import admin
from .models import Product, Supplier, SupplyOrder

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')

@admin.register(SupplyOrder)
class SupplyOrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'supplier', 'quantity', 'status', 'order_date')
    list_filter = ('status', 'order_date')
