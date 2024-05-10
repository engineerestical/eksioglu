from django.contrib import admin
from .models import Payment, PaymentSubject

@admin.register(PaymentSubject)
class PaymentSubjectAdmin(admin.ModelAdmin):
    list_display = ('payment_subject',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_type', 'case', 'payment_subject', 'payment_channel', 'payment_amount', 'payment_date', 'created_at', 'updated_at', 'created_by', 'last_updated_by')
    list_filter = ('payment_type', 'payment_date', 'created_at', 'updated_at', 'created_by', 'last_updated_by')
    search_fields = ('payment_type', 'case__name', 'payment_subject__payment_subject', 'payment_amount')
    readonly_fields = ('created_at', 'updated_at')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('created_by', 'last_updated_by')
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created
            obj.created_by = request.user
        obj.last_updated_by = request.user
        super().save_model(request, obj, form, change)
