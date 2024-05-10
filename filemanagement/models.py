from django.db import models
from usermanagement.models import CustomUser
from leadmanagement.models import Lead, Vehicle
from django.utils.translation import gettext_lazy as _
from staffmanagement.models import ExpertStaff, OfficeStaff, FieldStaff
from django.core.validators import RegexValidator
from django.utils import timezone
from datetime import timedelta, date
from django.db.models import Sum

# Create your models here.

class CustomInsuranceApplicationIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        kwargs.setdefault('unique', True)
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if add and not getattr(model_instance, self.attname):
            # Get the latest insurance application
            last_insurance_application = InsuranceApplication.objects.order_by('-id').first()
            if last_insurance_application:
                last_id = int(last_insurance_application.insurance_application_id.split('-')[-1])
                new_id = last_id + 1
                new_insurance_application_id = f'SB-{str(new_id).zfill(5)}'
            else:
                new_insurance_application_id = 'SB-00001'
            
            # Check if the new insurance application ID already exists
            while InsuranceApplication.objects.filter(insurance_application_id=new_insurance_application_id).exists():
                new_id += 1
                new_insurance_application_id = f'SB-{str(new_id).zfill(5)}'

            setattr(model_instance, self.attname, new_insurance_application_id)
            return new_insurance_application_id
        return super().pre_save(model_instance, add)


class InsuranceCompany(models.Model):
    insurance_company_name = models.CharField(_('Sigorta Şirketi Adı'), max_length=100, unique=True)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_sigorta_sirketleri", on_delete=models.SET_NULL, null=True, editable=False)
    last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_sigorta_sirketleri", on_delete=models.SET_NULL, null=True, editable=False)

    class Meta:
        verbose_name = _('Sigorta Şirketi')
        verbose_name_plural = _('Sigorta Şirketleri')

    def __str__(self):
        return self.insurance_company_name
    
    def save(self, *args, **kwargs):
        # Extracting the user object passed as a keyword argument
        user = kwargs.pop('user', None)
        
        # If the object is being created and a user is provided
        if not self.pk and user:
            self.created_by_id = user.id  # Assuming CustomUser has an 'id' field
        # If the object is being updated and a user is provided
        elif user:
            self.last_updated_by_id = user.id  # Assuming CustomUser has an 'id' field
            
        super().save(*args, **kwargs)


class CaseSubject(models.Model):
    subject = models.CharField(_('Dava Konusu'), max_length=100)
    distraint = models.BooleanField(_('İcra Konusu'), default=False)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_dava_konulari", on_delete=models.SET_NULL, null=True, editable=False)
    last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_dava_konulari", on_delete=models.SET_NULL, null=True, editable=False)

    class Meta:
        verbose_name = _('Dava Konusu')
        verbose_name_plural = _('Dava Konuları')

    def __str__(self):
        return self.subject
    
    def save(self, *args, **kwargs):
        # Extracting the user object passed as a keyword argument
        user = kwargs.pop('user', None)
        
        # If the object is being created and a user is provided
        if not self.pk and user:
            self.created_by_id = user.id  # Assuming CustomUser has an 'id' field
        # If the object is being updated and a user is provided
        elif user:
            self.last_updated_by_id = user.id  # Assuming CustomUser has an 'id' field
            
        super().save(*args, **kwargs)


class InsuranceType(models.Model):
    insurance_type = models.CharField(_('Sigorta Türü'), max_length=100, unique=True)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_sigorta_turleri", on_delete=models.SET_NULL, null=True, editable=False)
    last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_sigorta_turleri", on_delete=models.SET_NULL, null=True, editable=False)

    class Meta:
        verbose_name = _('Sigorta Türü')
        verbose_name_plural = _('Sigorta Türleri')

    def __str__(self):
        return self.insurance_type
    
    def save(self, *args, **kwargs):
        # Extracting the user object passed as a keyword argument
        user = kwargs.pop('user', None)
        
        # If the object is being created and a user is provided
        if not self.pk and user:
            self.created_by_id = user.id  # Assuming CustomUser has an 'id' field
        # If the object is being updated and a user is provided
        elif user:
            self.last_updated_by_id = user.id  # Assuming CustomUser has an 'id' field
            
        super().save(*args, **kwargs)



class CustomBuroNoField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        kwargs.setdefault('unique', True)
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if not value:
            last_buro_no = Case.objects.order_by('-id').first()  # Get the latest case
            if last_buro_no:
                last_id = int(last_buro_no.office_id.split('-')[-1])  # Extract the numeric part
                new_id = last_id + 1
                new_buro_no = f'B-{str(new_id).zfill(5)}'
            else:
                new_buro_no = 'B-00001'
            
            # Check if the new Büro No already exists
            while Case.objects.filter(office_id=new_buro_no).exists():
                new_id += 1
                new_buro_no = f'B-{str(new_id).zfill(5)}'

            setattr(model_instance, self.attname, new_buro_no)
            return new_buro_no
        return value


class Case(models.Model):
    
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE, verbose_name=_('Sigorta Şirketi'))
    case_subject = models.ForeignKey(CaseSubject, on_delete=models.CASCADE, verbose_name=_('Dava Konusu'))
    insurance_type = models.ForeignKey(InsuranceType, on_delete=models.CASCADE, verbose_name=_('Sigorta Türü'))
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, verbose_name=_('Müvekkil'))
    office_id = CustomBuroNoField(_('Büro No'), null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name=_('Araç'))
    accident_date = models.DateField(_('Kaza Tarihi'))
    claimed_lost_amount = models.DecimalField(_('Talep Edilen DK Tutarı'), max_digits=10, decimal_places=2, null=True, blank=True)
    insurance_application_date = models.DateField(_('Sigorta Başvuru Tarihi'), null=True, blank=True)
    arbitration_application_date = models.DateField(_('Tahkim Başvuru Tarihi'), null=True, blank=True)
    office_representative = models.ForeignKey(OfficeStaff, on_delete=models.CASCADE, verbose_name=_('Ofis Sorumlusu'))
    field_representative = models.ForeignKey(FieldStaff, on_delete=models.CASCADE, verbose_name=_('Saha Ekibi'))
    expert_representative = models.ForeignKey(ExpertStaff, on_delete=models.CASCADE, verbose_name=_('Usta/Servis'))
    be_subject_to_insurance_application = models.BooleanField(_("Sigorta Başvurusuna Tabi Dosya"), default=True)
    be_subject_to_arbitration_application = models.BooleanField(_("Tahkim Başvurusuna Tabi Dosya"), default=True)
    
    is_closed = models.BooleanField(_("Kapanan Dosya"), default=False)
    is_closed_with_pre_payment = models.BooleanField(_("Ön Ödeme ile Kapanan Dosya"), default=False)
    is_waiting_payment = models.BooleanField(_("İşlemi Biten Ödeme Bekleyen Dosya"), default=False)
    is_personel_lien = models.BooleanField(_("Şahsa İcra"), default=False)
    have_pre_payment = models.BooleanField(_("Ön Ödemeli"), default=False)
    closed_at = models.DateField(_('Dosya Kapanma Tarihi'), null=True, blank=True)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_dosyalar", on_delete=models.SET_NULL, null=True, editable=False)
    last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_dosyalar", on_delete=models.SET_NULL, null=True, editable=False)
    

    @property
    def remaining_days_to_insurance_application(self):
        """
        Calculates the remaining days until the insurance application deadline.
        """
        # Define the deadline duration (in days)
        deadline_duration = 15
        
        # Calculate the difference between today's date and the creation date of the case
        days_since_creation = (timezone.now().date() - self.created_at.date()).days
        
        # Calculate the remaining days until the insurance application deadline
        remaining_days = max(deadline_duration - days_since_creation, 0) if not self.insurance_application_date else -1
        
        return remaining_days if self.be_subject_to_insurance_application else -1 
    remaining_days_to_insurance_application.fget.short_description = 'Sigorta Başvurusuna Kalan Gün Sayısı'
    
    @property
    def remaining_days_to_arbitration_application(self):
        """
        Calculates the remaining days until the arbitration application deadline.
        """
        # Define the deadline duration (in days)
        deadline_duration = 15
        
        # Calculate the difference between the insurance application date and today's date
        if self.insurance_application_date:
            if self.insurance_type and "trafik" in self.insurance_type.insurance_type.lower():
                # Calculate remaining days as calendar days
                days_since_application = (timezone.now().date() - self.insurance_application_date).days
                remaining_days = max(deadline_duration - days_since_application, 0)
            elif self.insurance_type and "kasko" in self.insurance_type.insurance_type.lower():
                # Calculate remaining workdays (Monday to Friday)
                remaining_workdays = deadline_duration
                current_date = timezone.now().date()
                while remaining_workdays > 0:
                    current_date += timedelta(days=1)
                    if current_date.weekday() < 5:  # Monday to Friday
                        remaining_workdays -= 1
                remaining_days = max(remaining_workdays, 0)
            else:
                remaining_days = -1
        else:
            remaining_days = -1
        
        return remaining_days if self.be_subject_to_arbitration_application else -1

    remaining_days_to_arbitration_application.fget.short_description = 'Tahkim Başvurusuna Kalan Gün Sayısı'
    
    @property
    def latency_on_insurance_application(self):
        return True if self.remaining_days_to_insurance_application == 0 else False
    
    latency_on_insurance_application.fget.boolean = True
    
    latency_on_insurance_application.fget.short_description = 'Sigorta Başvurusu Gecikme Durumu'

    
    @property
    def latency_on_arbitration_application(self):
        return True if self.remaining_days_to_arbitration_application == 0 else False
    
    latency_on_arbitration_application.fget.boolean = True

    latency_on_arbitration_application.fget.short_description = 'Tahkim Başvurusu Gecikme Durumu'

    
    @property
    def profit_quantity(self):
        income_total = self.payment_set.filter(payment_type='I').aggregate(total=Sum('payment_amount'))['total'] or 0
        outcome_total = self.payment_set.filter(payment_type='O').aggregate(total=Sum('payment_amount'))['total'] or 0
        return income_total - outcome_total
    
    profit_quantity.fget.short_description = 'Kar/Zarar Durumu'
    
    @property
    def is_power_of_attorney_file(self):
        return True if self.lead.power_of_attorney_status == True else False
    
    is_power_of_attorney_file.fget.boolean = True
    
    is_power_of_attorney_file.fget.short_description = 'Vekalet Dosya'
        

    class Meta:
        verbose_name = _('Dosya')
        verbose_name_plural = _('Dosyalar')

    def __str__(self):
        return f"{self.office_id} - {self.lead.name_company_name}"
    
    def save(self, *args, **kwargs):
        # Extracting the user object passed as a keyword argument
        user = kwargs.pop('user', None)
        
        # If the object is being created and a user is provided
        if not self.pk and user:
            self.created_by_id = user.id  # Assuming CustomUser has an 'id' field
        # If the object is being updated and a user is provided
        elif user:
            self.last_updated_by_id = user.id  # Assuming CustomUser has an 'id' field
            
        super().save(*args, **kwargs)



class InsuranceApplication(models.Model):
    insurance_application_id = CustomInsuranceApplicationIDField(_('Sigorta Başvuru Ofis No'), null=True, blank=True, editable=False)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name=_('Dosya'))
    insurance_application_date = models.DateField(_('Sigorta Başvuru Tarihi'))
    insurance_application_status = models.CharField(_('Sigorta Başvuru Durumu'), max_length=100)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_sigorta_basvurulari", on_delete=models.SET_NULL, null=True, editable=False)
    last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_sigorta_basvurulari", on_delete=models.SET_NULL, null=True, editable=False)

    class Meta:
        verbose_name = _('Sigorta Başvurusu')
        verbose_name_plural = _('Sigorta Başvuruları')

    def __str__(self):
        return f'{self.case.office_id} - {self.insurance_application_date}'
    
    def save(self, *args, **kwargs):
        # Extracting the user object passed as a keyword argument
        user = kwargs.pop('user', None)
        
        # If the object is being created and a user is provided
        if not self.pk and user:
            self.created_by_id = user.id  # Assuming CustomUser has an 'id' field
        # If the object is being updated and a user is provided
        elif user:
            self.last_updated_by_id = user.id  # Assuming CustomUser has an 'id' field


        if self.case and self.insurance_application_date:
            self.case.insurance_application_date = self.insurance_application_date
            self.case.save(update_fields=['insurance_application_date'])

        super().save(*args, **kwargs)


class ArbitrationApplication(models.Model):
    arbitration_id = models.TextField(_('Esas No'))
    case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name=_('Dosya'))
    insurance_application = models.ForeignKey(InsuranceApplication, on_delete=models.CASCADE, verbose_name=_('Sigorta Başvurusu'), null=True, blank= True)
    arbitration_application_date = models.DateField(_('Tahkim Başvuru Tarihi'))
    arbitration_application_status = models.CharField(_('Tahkim Başvuru Durumu'), max_length=100, blank=True)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_tahkim_basvurulari", on_delete=models.SET_NULL, null=True, editable=False)
    last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_tahkim_basvurulari", on_delete=models.SET_NULL, null=True, editable=False)

    class Meta:
        verbose_name = _('Tahkim Başvurusu')
        verbose_name_plural = _('Tahkim Başvuruları')

    def __str__(self):
        return f'{self.case.office_id} - {self.arbitration_application_date}'
    
    def save(self, *args, **kwargs):
        # Extracting the user object passed as a keyword argument
        user = kwargs.pop('user', None)
        
        # If the object is being created and a user is provided
        if not self.pk and user:
            self.created_by_id = user.id  # Assuming CustomUser has an 'id' field
        # If the object is being updated and a user is provided
        elif user:
            self.last_updated_by_id = user.id  # Assuming CustomUser has an 'id' field
            
        super().save(*args, **kwargs)
