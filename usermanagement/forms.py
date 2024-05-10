from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import OfficeStaffUser, ExpertStaffUser, FieldStaffUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = OfficeStaffUser
        fields = ('username', 'email', 'national_identity_number', 'phone_number', 'hire_date')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = OfficeStaffUser
        fields = ('username', 'email', 'national_identity_number', 'phone_number', 'hire_date')

class OfficeStaffUserCreationForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = OfficeStaffUser

class OfficeStaffUserChangeForm(CustomUserChangeForm):
    class Meta(CustomUserChangeForm.Meta):
        model = OfficeStaffUser

class ExpertStaffUserCreationForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = ExpertStaffUser

class ExpertStaffUserChangeForm(CustomUserChangeForm):
    class Meta(CustomUserChangeForm.Meta):
        model = ExpertStaffUser

class FieldStaffUserCreationForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = FieldStaffUser

class FieldStaffUserChangeForm(CustomUserChangeForm):
    class Meta(CustomUserChangeForm.Meta):
        model = FieldStaffUser
