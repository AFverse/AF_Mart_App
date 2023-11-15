from django.contrib import admin
from django.contrib.admin import register 

from backend.models import * 

@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone', 'fullname', 'created_at']

@register(OTP)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'otp', 'validity', 'verified']

@register(Token)
class UserAdmin(admin.ModelAdmin):
    list_display = ['token', 'user', 'created_at']
    
@register(PassResetToken)
class UserAdmin(admin.ModelAdmin):
    list_display = ['token', 'user', 'validity', 'created_at']
    
@register(ParentCategory)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'disc', 'created_at']
    
@register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'disc', 'parent_category', 'created_at']
    
@register(Reviews)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'created_at']
    
@register(Discount)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'start_date', 'end_date']
    
@register(Brand)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    
@register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'brand', 'inventory', 'created_at']
    
@register(ProductVariation)
class UserAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'price', 'created_at']
    
@register(Cart_itmes)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'created_at']
    
@register(OrderItems)
class UserAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'created_at']
    
@register(Order)
class UserAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'status', 'created_at']

@register(UserItem)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'is_in_cart' , 'created_at']

