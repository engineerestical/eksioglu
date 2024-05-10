from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Lead, Vehicle, PowerOfAttorney

class LeadAdmin(ImportExportModelAdmin):
    list_display = ('name_company_name', 'national_id', 'lead_type', 'is_active', 'get_total_number_of_cases')
    list_filter = ('lead_type', 'is_active')
    search_fields = ('name_company_name', 'national_id')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'last_updated_by', 'power_of_attorney_status')

    def save_model(self, request, obj, form, change):
        # If the object is being created
        if not obj.pk:
            obj.created_by = request.user
        # If the object is being updated
        else:
            obj.last_updated_by = request.user
        obj.save()

admin.site.register(Lead, LeadAdmin)

class VehicleAdmin(ImportExportModelAdmin):
    list_display = ('number_plate', 'brand', 'color', 'lead', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('number_plate', 'brand', 'color')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'last_updated_by')
    
    def save_model(self, request, obj, form, change):
        # If the object is being created
        if not obj.pk:
            obj.created_by = request.user
        # If the object is being updated
        else:
            obj.last_updated_by = request.user
        obj.save()

admin.site.register(Vehicle, VehicleAdmin)

class PowerOfAttorneyAdmin(ImportExportModelAdmin):
    list_display = ('lead', 'power_of_attorney_startdate', 'power_of_attorney_enddate')
    list_filter = ('power_of_attorney_startdate', 'power_of_attorney_enddate')
    search_fields = ('lead', 'power_of_attorney_startdate', 'power_of_attorney_enddate')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'last_updated_by', 'is_active')
    
    def save_model(self, request, obj, form, change):
        # If the object is being created
        if not obj.pk:
            obj.created_by = request.user
        # If the object is being updated
        else:
            obj.last_updated_by = request.user
        obj.save()

admin.site.register(PowerOfAttorney, PowerOfAttorneyAdmin)
