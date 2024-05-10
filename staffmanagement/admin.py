from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from .models import Department, Region, OfficeStaff, ExpertStaff, FieldStaff
from import_export import resources
from import_export.widgets import ForeignKeyWidget

class DepartmentResource(resources.ModelResource):
    """
    Resource class for Department model.
    """
    class Meta:
        
        fields = ('id', 'department_name')
        export_order = ('id', 'department_name')
        model = Department
        
@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    """
    Admin class for Department model with import-export functionality.
    """
    resource_classes = [DepartmentResource]
    list_display = ('department_name',)
    search_fields = ('department_name',)


class RegionResource(resources.ModelResource):
    """
    Resource class for Region model.
    """
    class Meta:
        model = Region
        fields = ('id', 'region_name')
        export_order = ('id', 'region_name')

@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    """
    Admin class for Region model with import-export functionality.
    """
    resource_classes = [RegionResource]
    list_display = ('region_name',)
    search_fields = ('region_name',)

class OfficeStaffResource(resources.ModelResource):
    """
    Resource class for OfficeStaff model.
    """
    class Meta:
        model = OfficeStaff
        # Define fields to export
        fields = ('id', 'first_name', 'last_name', 'email', 'national_identity_number', 'phone_number', 'department', 'hire_date', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'first_name', 'last_name', 'email', 'national_identity_number', 'phone_number', 'department', 'hire_date', 'is_active', 'created_at', 'updated_at')

@admin.register(OfficeStaff)
class OfficeStaffAdmin(ImportExportModelAdmin):
    """
    Admin class for OfficeStaff model with import-export functionality.
    """
    resource_classes = [OfficeStaffResource]
    list_display = ('first_name', 'last_name', 'email', 'national_identity_number', 'phone_number', 'department', 'hire_date', 'is_active', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'national_identity_number', 'phone_number')
    list_filter = ('department', 'hire_date', 'is_active', 'created_at', 'updated_at')

class ExpertStaffResource(resources.ModelResource):
    region= Field(
        column_name='sigorta_turu',
        attribute='sigorta_turu',
        widget=ForeignKeyWidget(Region,'region_name')
    )
    class Meta:
        model = ExpertStaff
        fields = ('id', 'first_name', 'last_name', 'email', 'national_identity_number', 'phone_number', 'region', 'hire_date', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'first_name', 'last_name', 'email', 'national_identity_number', 'phone_number', 'region', 'hire_date', 'is_active', 'created_at', 'updated_at')

@admin.register(ExpertStaff)
class ExpertStaffAdmin(ImportExportModelAdmin):
    """
    Admin class for ExpertStaff model with import-export functionality.
    """
    resource_classes = [ExpertStaffResource]
    list_display = ('first_name', 'last_name', 'email', 'national_identity_number', 'phone_number', 'region', 'hire_date', 'is_active', 'created_at', 'updated_at', 'get_aggregated_profit_quantity')
    search_fields = ('first_name', 'last_name', 'email', 'national_identity_number', 'phone_number')
    list_filter = ('region', 'hire_date', 'is_active', 'created_at', 'updated_at')

    def get_aggregated_profit_quantity(self, obj):
        """
        Display the aggregated profit quantity for the field representative.
        """
        return obj.get_aggregated_profit_quantity()

    get_aggregated_profit_quantity.short_description = 'Kar/Zarar Miktarı'

class FieldStaffResource(resources.ModelResource):
    region= Field(
        column_name='sigorta_turu',
        attribute='sigorta_turu',
        widget=ForeignKeyWidget(Region,'region_name')
    )
    class Meta:
        model = FieldStaff
        fields = ('id', 'first_name', 'last_name', 'email', 'national_identity_number', 'phone_number', 'region', 'hire_date', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'first_name', 'last_name', 'email', 'national_identity_number', 'phone_number', 'region', 'hire_date', 'is_active', 'created_at', 'updated_at')


@admin.register(FieldStaff)
class FieldStaffAdmin(ImportExportModelAdmin):
    """
    Admin class for FieldStaff model with import-export functionality.
    """
    resource_classes = [FieldStaffResource]
    list_display = ('first_name', 'last_name', 'email', 'national_identity_number', 'phone_number', 'region', 'hire_date', 'is_active', 'created_at', 'updated_at', 'get_aggregated_profit_quantity')

    def get_aggregated_profit_quantity(self, obj):
        """
        Display the aggregated profit quantity for the field representative.
        """
        return obj.get_aggregated_profit_quantity()

    get_aggregated_profit_quantity.short_description = 'Kar/Zarar Miktarı'
