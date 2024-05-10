import os
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from staffmanagement.models import OfficeStaff, ExpertStaff, FieldStaff
from usermanagement.models import CustomUser
from django.utils import timezone

PERSON = 'P'
COMPANY = 'C'
MUVEKKIL_TYPE_CHOICES = [
    (PERSON, 'Şahıs'),
    (COMPANY, 'Şirket'),
]

class Lead(models.Model):
    lead_type = models.CharField(_("Müvekkil Tipi"), max_length=1, choices=MUVEKKIL_TYPE_CHOICES)
    name_company_name = models.CharField(_("İsim Soyisim/Şirket Adı"), max_length=255, blank=True)
    national_id = models.PositiveIntegerField(_("Tc Kimlik/Vergi No"), blank=True, null=True)
    phone = models.CharField(_("Telefon Numarası"), max_length=15, blank=True)
    alternate_phone = models.CharField(_("Alternatif Telefon Numarası"), max_length=15, blank=True)
    lead_email = models.EmailField(_("Eposta"), max_length=254, blank=True)
    iban_number = models.CharField(_("IBAN No"), max_length=50, blank=True)
    logo = models.ImageField(_("Logo"), upload_to='logos/', blank=True, null=True)
    is_active = models.BooleanField(_("Aktif"), default=True)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_muvekkiller", on_delete=models.SET_NULL, null=True, editable=False)
    last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_muvekkiller", on_delete=models.SET_NULL, null=True, editable=False)

    @property
    def power_of_attorney_status(self):
        # Check if any associated PowerOfAttorney objects have an end_date greater than today's date
        today = timezone.now().date()
        return self.powerofattorney_set.filter(power_of_attorney_enddate__gt=today).exists()
    def get_total_number_of_cases(self):
        
        # Import Case model here to avoid circular imports
        from filemanagement.models import Case
        
        # Get all the cases related to the field representative
        related_cases = Case.objects.filter(lead=self)

        # Calculate the aggregated profit quantity
        total_number_of_cases = related_cases.count()

        return total_number_of_cases
    
    get_total_number_of_cases.short_description = 'Toplam Dosya Sayısı'

    
    class Meta:
        verbose_name = _("Müvekkil")
        verbose_name_plural = _("Müvekkiller")

    def __str__(self):
        return f"{self.name_company_name} {self.national_id}"

    def get_absolute_url(self):
        return reverse("Lead_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        # Extracting the user object passed as a keyword argument
        user = kwargs.pop('user', None)

        if self.logo:
            filename = f"{self.name_company_name}_{self.national_id}_logo{os.path.splitext(self.logo.name)[1]}"
            self.logo.name = self._get_unique_logo_filename(filename)
        
        # If the object is being created and a user is provided
        if not self.pk and user:
            self.created_by_id = user.id  # Assuming CustomUser has an 'id' field
        # If the object is being updated and a user is provided
        elif user:
            self.last_updated_by_id = user.id  # Assuming CustomUser has an 'id' field
            
        super().save(*args, **kwargs)

    def _get_unique_logo_filename(self, filename):
        # Function to ensure filename is unique
        if self._meta.model.objects.filter(logo=filename):
            # If a file with the same name exists, add a unique identifier
            name, ext = os.path.splitext(filename)
            count = 1
            while self._meta.model.objects.filter(logo=f"{name}_{count}{ext}").exists():
                count += 1
            return f"{name}_{count}{ext}"
        return filename
    
class Vehicle(models.Model):
    number_plate = models.CharField(_("Plaka"), max_length=50, blank=True)
    brand = models.CharField(_("Marka/Model"), max_length=50, blank=True)
    color = models.CharField(_("Renk"), max_length=50, blank=True)
    lead = models.ForeignKey("Lead", verbose_name=_("Müvekkil"), on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(_("Aktif"), default=True)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_araclar", on_delete=models.SET_NULL, null=True, editable=False)
    last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_araclar", on_delete=models.SET_NULL, null=True, editable=False)

    class Meta:
        verbose_name = _("Araç")
        verbose_name_plural = _("Araçlar")

    def __str__(self):
        return self.number_plate

    def get_absolute_url(self):
        return reverse("Araç_detay", kwargs={"pk": self.pk})

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

class PowerOfAttorney(models.Model):
    lead = models.ForeignKey("Lead", verbose_name=_("Müvekkil"), on_delete=models.CASCADE, null=True)
    power_of_attorney_startdate = models.DateField(_("Vekalet Başlangıç Tarihi"), auto_now=False, auto_now_add=False)
    power_of_attorney_enddate = models.DateField(_("Vekalet Bitiş Tarihi"), auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_vekaletler", on_delete=models.SET_NULL, null=True, editable=False)
    last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_vekaletler", on_delete=models.SET_NULL, null=True, editable=False)

    @property
    def is_active(self):
        # Get today's date
        today = timezone.now().date()
        
        # Check if start and end dates are not None
        if self.power_of_attorney_startdate is None or self.power_of_attorney_enddate is None:
            return False
        
        # Check if today's date is between startdate and enddate
        return self.power_of_attorney_startdate <= today <= self.power_of_attorney_enddate
        
    is_active.fget.short_description = 'Aktiflik Durumu'
    
    class Meta:
        verbose_name = _("Vekalet")
        verbose_name_plural = _("Vekaletler")

    def __str__(self):
        return f"{self.lead.name_company_name}_{self.power_of_attorney_startdate}_{self.power_of_attorney_enddate}"

    def get_absolute_url(self):
        return reverse("Vekalet_detay", kwargs={"pk": self.pk})

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