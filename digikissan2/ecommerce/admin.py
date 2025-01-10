from django.contrib import admin
from .models import Create_Seller_Account,Tag,Products

@admin.register(Create_Seller_Account)
class SellerAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'business_name', 'bank_name', 'verification_status', 'total_sales', 'rating', 'is_active')
    search_fields = ('user__username', 'business_name')
    list_filter = ('verification_status', 'categories', 'is_active')
    

@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ['name']
    
    
@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'stock_quantity', 'status', 'average_ratings', 'date_added', 'is_fetuared']

    