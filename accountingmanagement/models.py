from django.db import models
from django.utils.translation import gettext_lazy as _
from usermanagement.models import CustomUser
from filemanagement.models import Case


INCOME = 'I'
OUTCOME = 'O'
INCOME_OUTCOME_CHOICES = [
    (INCOME, 'Gelir'),
    (OUTCOME, 'Gider'),
]

BANKTRANSFER = 'B'
CASH = 'C'
LAWYERCARD = 'LC'
PAYMENT_CHANNEL_CHOICES = [
    (BANKTRANSFER, 'EFT/Havele'),
    (CASH, 'Nakit'),
    (LAWYERCARD, 'Barokart'),
]

class PaymentSubject(models.Model):
    payment_subject = models.CharField(_('Ödeme Tipi'), max_length=100)

    class Meta:
        verbose_name = _('Ödeme Tipi')
        verbose_name_plural = _('Ödeme Tipleri')

    def __str__(self):
        return self.payment_subject

class PaymentCategory(models.Model):
    payment_category = models.CharField(_('Ödeme Kategorisi'), max_length=100)

    class Meta:
        verbose_name = _('Ödeme Kategorisi')
        verbose_name_plural = _('Ödeme Kategorileri')

    def __str__(self):
        return self.payment_category

class Payment(models.Model):
    payment_type = models.CharField(_('Gelir/Gider'), max_length=20, choices=INCOME_OUTCOME_CHOICES)
    payment_channel = models.CharField(_('Ödeme Kanalı'), max_length=20, choices=PAYMENT_CHANNEL_CHOICES, null=True, blank=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name=_('Dosya'))
    payment_subject = models.ForeignKey(PaymentSubject, on_delete=models.CASCADE, verbose_name=_('Ödeme Tipi'))
    payment_category = models.ForeignKey(PaymentCategory, on_delete=models.CASCADE, verbose_name=_('Ödeme Kategorisi'), null=True, blank=True)
    payment_amount = models.DecimalField(_('Ödeme Miktarı'), max_digits=10, decimal_places=2)
    payment_date = models.DateField(_('Ödeme Tarihi'))
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_odemeler", on_delete=models.SET_NULL, null=True, editable=False)
    last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_odemeler", on_delete=models.SET_NULL, null=True, editable=False)

    class Meta:
        verbose_name = _('Ödeme')
        verbose_name_plural = _('Ödemeler')

    def __str__(self):
        return f'{self.payment_type} - {self.payment_amount} - {self.payment_date}'
    
    def save(self, *args, **kwargs):
        # Extracting the user object passed as a keyword argument
        user = kwargs.pop('user', None)
        
        # If the object is being created and a user is provided
        if not self.pk and user:
            self.created_by_id = user.id 
        # If the object is being updated and a user is provided
        elif user:
            self.last_updated_by_id = user.id 
            
        super().save(*args, **kwargs)
