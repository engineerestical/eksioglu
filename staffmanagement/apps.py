from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StaffmanagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staffmanagement'
    verbose_name = _('Personel Yönetimi')
