from django.contrib import admin
from .models import CaseStatistics

class CaseStatisticsAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    # Override queryset to ensure only one instance of CaseStatistics is displayed
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(pk=1)

    # Override has_add_permission to prevent adding new instances through the admin
    def has_add_permission(self, request):
        return False

    # Override has_delete_permission to prevent deleting the instance through the admin
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(CaseStatistics, CaseStatisticsAdmin)
