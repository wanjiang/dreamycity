from django.contrib import admin
from store.models import StoreCategory, Supplier, StoreItem, OrderItem, Order

# Register your models here.
admin.site.register(StoreCategory)
admin.site.register(Supplier)
admin.site.register(StoreItem)
admin.site.register(OrderItem)
admin.site.register(Order)