from django.contrib import admin
from django.contrib.admin import register 
from authentication.models import *
# Register your models here.

@register(cUser)
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
    