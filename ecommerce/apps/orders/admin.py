from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "full_name", "email", "billing_status", "created"]
    list_filter = ["user", "email", "billing_status", "created"]
    # search_fields = ["first_name", "last_name", "email", "address", "zipcode", "place", "phone"]
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "product", "price", "quantity"]
    list_filter = ["order", "product", "price", "quantity"]
