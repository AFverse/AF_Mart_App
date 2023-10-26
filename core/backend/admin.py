from django.contrib import admin
from django.contrib.admin import register 

from backend.models import * 

@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone', 'fullname', 'created_at']

@register(OTP)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'otp', 'validity', 'verified']
