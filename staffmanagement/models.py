from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
#from usermanagement.models import CustomUser


class Department(models.Model):
    department_name = models.CharField(_("Departman Adı"), max_length=50)
    class Meta:
        verbose_name = _("Departman")
        verbose_name_plural = _("Departmanlar")

    def __str__(self):
        return self.department_name

    def get_absolute_url(self):
        return reverse("Department_detail", kwargs={"pk": self.pk})

class Region(models.Model):
    region_name = models.CharField(_("Bölge Adı"), max_length=50)
    class Meta:
        verbose_name = _("Bölge")
        verbose_name_plural = _("Bölgeler")

    def __str__(self):
        return self.region_name

    def get_absolute_url(self):
        return reverse("Region_detail", kwargs={"pk": self.pk})


class OfficeStaff(models.Model):
    first_name = models.CharField(_("İsim"), max_length=100)
    last_name = models.CharField(_("Soyisim"), max_length=100)
    email = models.EmailField(_("Eposta"), max_length=254)
    national_identity_number = models.CharField(_("TC Kimlik No"), max_length=11)
    phone_number = models.CharField(_("Telefon Numarası"), max_length=15)
    department = models.ForeignKey(Department, verbose_name=_("Departman"), on_delete=models.CASCADE)
    hire_date = models.DateField(_("İşe Alım Tarihi"), auto_now=False, auto_now_add=False)
    is_active = models.BooleanField(_("Aktif"), default = True)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    #created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_ofis_personeli", on_delete=models.SET_NULL, null=True, editable=False)
    #last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_ofis_personeli", on_delete=models.SET_NULL, null=True, editable=False)


    class Meta:
        verbose_name = _("Ofis Personeli")
        verbose_name_plural = _("Ofis Personelleri")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("OfficeStaff_detail", kwargs={"pk": self.pk})

class ExpertStaff(models.Model):
    first_name = models.CharField(_("İsim"), max_length=100, null=True, blank=True)
    last_name = models.CharField(_("Soyisim"), max_length=100, null=True, blank=True)
    email = models.EmailField(_("Eposta"), max_length=254, null=True, blank=True)
    national_identity_number = models.CharField(_("TC Kimlik No"), max_length=11, null=True, blank=True)
    phone_number = models.CharField(_("Telefon Numarası"), max_length=15, null=True, blank=True)
    region = models.ForeignKey(Region, verbose_name=_("Bölge"), on_delete=models.CASCADE, null=True, blank=True)
    hire_date = models.DateField(_("İşe Alım Tarihi"), auto_now=False, auto_now_add=False, null=True, blank=True)
    is_active = models.BooleanField(_("Aktif"), default = True)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    #created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_usta_servisler", on_delete=models.SET_NULL, null=True, editable=False)
    #last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_usta_servisler", on_delete=models.SET_NULL, null=True, editable=False)

    # def get_aggregated_profit_quantity(self):
    #     """
    #     Calculate the aggregated profit quantity for the field representative.
    #     """
    #     # Import Case model here to avoid circular imports
    #     from filemanagement.models import Case
        
    #     # Get all the cases related to the field representative
    #     related_cases = Case.objects.filter(expert_representative=self)

    #     # Calculate the aggregated profit quantity
    #     total_profit_quantity = sum(case.profit_quantity for case in related_cases)

    #     return total_profit_quantity
    
    # get_aggregated_profit_quantity.short_description = 'Kar/Zarar Miktarı'
    
    class Meta:
        verbose_name = _("Usta/Servis")
        verbose_name_plural = _("Usta/Servisler")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("ExpertStaff_detail", kwargs={"pk": self.pk})

class FieldStaff(models.Model):
    first_name = models.CharField(_("İsim"), max_length=100, null=True, blank=True)
    last_name = models.CharField(_("Soyisim"), max_length=100, null=True, blank=True)
    email = models.EmailField(_("Eposta"), max_length=254, null=True, blank=True)
    national_identity_number = models.CharField(_("TC Kimlik No"), max_length=11, null=True, blank=True)
    phone_number = models.CharField(_("Telefon Numarası"), max_length=15, null=True, blank=True)
    region = models.ForeignKey(Region, verbose_name=_("Bölge"), on_delete=models.CASCADE, null=True, blank=True)
    expert_staffs = models.ManyToManyField(ExpertStaff, verbose_name=_("Usta/Servisler"), null=True, blank=True)
    hire_date = models.DateField(_("İşe Alım Tarihi"), auto_now=False, auto_now_add=False, null=True, blank=True)
    is_active = models.BooleanField(_("Aktif"), default = True)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)
    # created_by = models.ForeignKey(CustomUser, verbose_name=_("Oluşturan"), related_name="olusturulan_saha_ekipleri", on_delete=models.SET_NULL, null=True, editable=False)
    # last_updated_by = models.ForeignKey(CustomUser, verbose_name=_("Son Güncelleyen"), related_name="son_guncellenen_saha_ekipleri", on_delete=models.SET_NULL, null=True, editable=False)

    # def get_aggregated_profit_quantity(self):
    #     """
    #     Calculate the aggregated profit quantity for the field representative.
    #     """
    #     # Import Case model here to avoid circular imports
    #     from filemanagement.models import Case
        
    #     # Get all the cases related to the field representative
    #     related_cases = Case.objects.filter(field_representative=self)

    #     # Calculate the aggregated profit quantity
    #     total_profit_quantity = sum(case.profit_quantity for case in related_cases)

    #     return total_profit_quantity
    
    # get_aggregated_profit_quantity.short_description = 'Kar/Zarar Miktarı'

    
    class Meta:
        verbose_name = _("Saha Personeli")
        verbose_name_plural = _("Saha Personelleri")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("FieldStaff_detail", kwargs={"pk": self.pk})