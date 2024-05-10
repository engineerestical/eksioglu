from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UsermanagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usermanagement'
    verbose_name = _('Kullanıcı Yönetimi')
