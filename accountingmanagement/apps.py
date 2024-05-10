from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AccountingmanagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accountingmanagement'
    verbose_name = _('Muhasebe Yönetimi')
