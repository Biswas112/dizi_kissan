from django.contrib import admin
from .models import Create_Seller_Account

@admin.register(Create_Seller_Account)
class SellerAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'busines_name', 'bank_name', 'verification_status', 'total_sales', 'rating', 'is_active')
    search_fields = ('user__username', 'busines_name')
    list_filter = ('verification_status', 'categories', 'is_active')
