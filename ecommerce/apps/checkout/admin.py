from django.contrib import admin

from .models import DeliveryOptions


@admin.register(DeliveryOptions)
class DeliveryOptionsAdmin(admin.ModelAdmin):
    list_display = ("delivery_name", "delivery_price", "is_active", "created_at", "updated_at")
    list_filter = ("delivery_name", "delivery_price", "is_active", "created_at", "updated_at")
