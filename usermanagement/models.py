from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError(_('Kullanıcı adı zorunludur'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser is_staff=True olmalıdır'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuseris_superuser=True olmalıdır'))

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=150, unique=True)
    email = models.EmailField(_('email address'), blank=True)
    national_identity_number = models.CharField(_("TC Kimlik No"), max_length=11)
    phone_number = models.CharField(_("Telefon Numarası"), max_length=15)
    hire_date = models.DateField(_("İşe Alım Tarihi"), auto_now=False, auto_now_add=False, null=True, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    created_at = models.DateTimeField(_("Oluşturma Zamanı"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Son Güncelleme Zamanı"), auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['national_identity_number', 'phone_number']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username


class OfficeStaffUser(CustomUser):
    department = models.ForeignKey(to='staffmanagement.Department', verbose_name=_("Departman"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Ofis Personeli")
        verbose_name_plural = _("Ofis Personelleri")


class ExpertStaffUser(CustomUser):
    region = models.ForeignKey(to='staffmanagement.Region', verbose_name=_("Bölge"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Usta/Servis")
        verbose_name_plural = _("Usta/Servisler")


class FieldStaffUser(CustomUser):
    region = models.ForeignKey(to='staffmanagement.Region', verbose_name=_("Bölge"), on_delete=models.CASCADE)
    expert_staffs = models.ManyToManyField(ExpertStaffUser, verbose_name=_("Usta/Servisler"))

    class Meta:
        verbose_name = _("Saha Personeli")
        verbose_name_plural = _("Saha Personelleri")