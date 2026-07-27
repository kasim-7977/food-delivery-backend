from django.contrib import admin
from .models import Category, Food, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "available")
    list_filter = ("category", "available")
    search_fields = ("name",)

admin.site.register(Order)
admin.site.register(OrderItem)