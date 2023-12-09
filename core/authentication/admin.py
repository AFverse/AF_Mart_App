from django.contrib import admin
from django.contrib.admin import register 
from .models import *

# Register your models here.

@register(cUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone']

@register(OTP)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'otp', 'validity', 'verified']

@register(Token)
class UserAdmin(admin.ModelAdmin):
    list_display = ['token', 'user', 'created_at']
    
@register(PassResetToken)
class UserAdmin(admin.ModelAdmin):
    list_display = ['token', 'user', 'validity', 'created_at']
    