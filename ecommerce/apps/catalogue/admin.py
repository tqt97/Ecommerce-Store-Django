from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (Category, Product, ProductImage, ProductSpecification,
                     ProductSpecificationValue, ProductType)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "is_active", "parent", "created_at", "updated_at"] 
    list_filter = ["name", "is_active", "parent", "created_at"]
    prepopulated_fields = {"slug": ("name",)}


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [ProductSpecificationInline]
    list_display = ["name", "created_at", "updated_at"]
    list_filter = ["name", "is_active","created_at"]


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSpecificationValueInline, ProductImageInline]
    list_display = ["title","product_type", "category", "is_active", "created_at", "updated_at"]
    list_filter = ["title", "is_active", "product_type", "category", "created_at"]
    prepopulated_fields = {"slug": ("title",)}
