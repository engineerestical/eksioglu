from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import OfficeStaffUser, ExpertStaffUser, FieldStaffUser
from django.utils.translation import gettext_lazy as _

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = OfficeStaffUser
    list_display = ('username', 'email', 'national_identity_number', 'phone_number', 'hire_date', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal Info'), {'fields': ('national_identity_number', 'phone_number', 'hire_date')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'national_identity_number', 'phone_number')
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(OfficeStaffUser, CustomUserAdmin)
admin.site.register(ExpertStaffUser, CustomUserAdmin)
admin.site.register(FieldStaffUser, CustomUserAdmin)