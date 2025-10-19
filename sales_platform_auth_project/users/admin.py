from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'full_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'profile_picture_url')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('full_name',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)