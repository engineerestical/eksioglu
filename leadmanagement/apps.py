from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class LeadmanagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leadmanagement'
    verbose_name = _('Müvekkil Yönetimi')
