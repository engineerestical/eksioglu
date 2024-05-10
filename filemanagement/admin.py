from django.contrib import admin
from .models import InsuranceCompany, CaseSubject, InsuranceType, Case, InsuranceApplication, ArbitrationApplication
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(InsuranceCompany)
class InsuranceCompanyAdmin(ImportExportModelAdmin):
    list_display = ('insurance_company_name', 'created_at', 'updated_at', 'created_by', 'last_updated_by')

@admin.register(CaseSubject)
class CaseSubjectAdmin(ImportExportModelAdmin):
    list_display = ('subject', 'distraint', 'created_at', 'updated_at', 'created_by', 'last_updated_by')

@admin.register(InsuranceType)
class InsuranceTypeAdmin(admin.ModelAdmin):
    list_display = ('insurance_type', 'created_at', 'updated_at', 'created_by', 'last_updated_by')

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('insurance_company', 'case_subject', 'insurance_type', 'lead', 'office_id', 'accident_date', 'insurance_application_date', 'arbitration_application_date', 'office_representative', 'field_representative', 'expert_representative', 'be_subject_to_insurance_application', 'be_subject_to_arbitration_application', 'created_at', 'updated_at', 'created_by', 'last_updated_by', 'remaining_days_to_insurance_application', 'remaining_days_to_arbitration_application', 'profit_quantity', 'latency_on_insurance_application', 'latency_on_arbitration_application', 'is_power_of_attorney_file')

@admin.register(InsuranceApplication)
class InsuranceApplicationAdmin(admin.ModelAdmin):
    list_display = ('case', 'insurance_application_date', 'insurance_application_status', 'created_at', 'updated_at', 'created_by', 'last_updated_by')

@admin.register(ArbitrationApplication)
class ArbitrationApplicationAdmin(admin.ModelAdmin):
    list_display = ('arbitration_id', 'case', 'arbitration_application_date', 'arbitration_application_status', 'created_at', 'updated_at', 'created_by', 'last_updated_by')
