from rest_framework import serializers
from reportmanagement.models import CaseStatistics
from leadmanagement.models import Lead, Vehicle, PowerOfAttorney
from accountingmanagement.models import PaymentCategory, PaymentSubject, Payment
from filemanagement.models import InsuranceCompany, CaseSubject, InsuranceType, Case, InsuranceApplication, ArbitrationApplication
from staffmanagement.models import Department, Region, OfficeStaff, ExpertStaff, FieldStaff
from reportmanagement.models import CaseStatistics

class LeadVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class LeadPowerOfAttorneySerializer(serializers.ModelSerializer):
    is_active =  serializers.ReadOnlyField()
    class Meta:
        model = PowerOfAttorney
        fields = '__all__'

class LeadCaseSerializer(serializers.ModelSerializer):
    remaining_days_to_insurance_application = serializers.ReadOnlyField()
    remaining_days_to_arbitration_application = serializers.ReadOnlyField()
    latency_on_insurance_application = serializers.ReadOnlyField()
    latency_on_arbitration_application = serializers.ReadOnlyField()
    profit_quantity = serializers.ReadOnlyField()
    is_power_of_attorney_file = serializers.ReadOnlyField()
    
    class Meta:
        model = Case
        fields = '__all__'



class LeadSerializer(serializers.ModelSerializer):
    power_of_attorney_status = serializers.ReadOnlyField()
    get_total_number_of_cases = serializers.ReadOnlyField()
    vehicles = serializers.SerializerMethodField(method_name='get_vehicles')
    power_of_attorneys = serializers.SerializerMethodField(method_name='get_power_of_attorneys')
    cases = serializers.SerializerMethodField(method_name='get_cases')
    
    class Meta:
        model = Lead
        fields = '__all__'
        extra_fields = ['vehicles', 'power_of_attorneys', 'cases']

    def get_vehicles(self, obj):
        vehicles  = Vehicle.objects.filter(lead=obj)
        serializer = LeadVehicleSerializer(vehicles, many=True)
        return serializer.data
    def get_power_of_attorneys(self, obj):
        power_of_attorneys  = PowerOfAttorney.objects.filter(lead=obj)
        serializer = LeadPowerOfAttorneySerializer(power_of_attorneys, many=True)
        return serializer.data
    def get_cases(self, obj):
        cases  = Case.objects.filter(lead=obj)
        serializer = LeadCaseSerializer(cases, many=True)
        return serializer.data

class VehicleSerializer(serializers.ModelSerializer):
    lead = LeadSerializer()
    class Meta:
        model = Vehicle
        fields = '__all__'

class PowerOfAttorneySerializer(serializers.ModelSerializer):
    lead = LeadSerializer()
    is_active =  serializers.ReadOnlyField()
    class Meta:
        model = PowerOfAttorney
        fields = '__all__'

class PaymentSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSubject
        fields = '__all__'

class PaymentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCategory
        fields = '__all__'



class InsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceCompany
        fields = '__all__'

class CaseSubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CaseSubject
        fields = '__all__'


class InsuranceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceType
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class OfficeStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeStaff
        fields = '__all__'


class ExpertStaffSerializer(serializers.ModelSerializer):
    get_aggregated_profit_quantity = serializers.ReadOnlyField()

    class Meta:
        model = ExpertStaff
        fields = '__all__'


class FieldStaffSerializer(serializers.ModelSerializer):
    get_aggregated_profit_quantity = serializers.ReadOnlyField()

    class Meta:
        model = FieldStaff
        fields = '__all__'

class CaseInsuranceApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceApplication
        fields = '__all__'

class CaseArbitrationApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArbitrationApplication
        fields = '__all__'

class CasePaymentSerializer(serializers.ModelSerializer):
    payment_subject = PaymentSubjectSerializer()
    payment_category = PaymentCategorySerializer()

    class Meta:
        model = Payment
        fields = '__all__'
    

class CaseLeadSerializer(serializers.ModelSerializer):
    power_of_attorney_status = serializers.ReadOnlyField()
    get_total_number_of_cases = serializers.ReadOnlyField()
    vehicles = serializers.SerializerMethodField(method_name='get_vehicles')
    power_of_attorneys = serializers.SerializerMethodField(method_name='get_power_of_attorneys')
    
    class Meta:
        model = Lead
        fields = '__all__'
        extra_fields = ['vehicles', 'power_of_attorneys', 'cases']

    def get_vehicles(self, obj):
        vehicles  = Vehicle.objects.filter(lead=obj)
        serializer = LeadVehicleSerializer(vehicles, many=True)
        return serializer.data
    def get_power_of_attorneys(self, obj):
        power_of_attorneys  = PowerOfAttorney.objects.filter(lead=obj)
        serializer = LeadPowerOfAttorneySerializer(power_of_attorneys, many=True)
        return serializer.data
    
class CaseVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
    
class CaseSerializer(serializers.ModelSerializer):
    remaining_days_to_insurance_application = serializers.ReadOnlyField()
    remaining_days_to_arbitration_application = serializers.ReadOnlyField()
    latency_on_insurance_application = serializers.ReadOnlyField()
    latency_on_arbitration_application = serializers.ReadOnlyField()
    profit_quantity = serializers.ReadOnlyField()
    is_power_of_attorney_file = serializers.ReadOnlyField()
    insurance_company = InsuranceCompanySerializer()
    case_subject = CaseSubjectSerializer()
    insurance_type = InsuranceTypeSerializer()
    lead = CaseLeadSerializer()
    office_representative = OfficeStaffSerializer()
    field_representative = FieldStaffSerializer()
    expert_representative = ExpertStaffSerializer()
    vehicle = CaseVehicleSerializer()
    insurance_applications = serializers.SerializerMethodField(method_name='get_insurance_applications')
    arbitration_applications = serializers.SerializerMethodField(method_name='get_arbitration_applications')
    payments = serializers.SerializerMethodField(method_name='get_payments')

    class Meta:
        model = Case
        fields = '__all__'
        extra_fields = ['insurance_applications', 'arbitration_applications', 'payments']

    def get_insurance_applications(self, obj):
        insurance_applications  = InsuranceApplication.objects.filter(case=obj)
        serializer = CaseInsuranceApplicationSerializer(insurance_applications, many=True)
        return serializer.data
    def get_arbitration_applications(self, obj):
        arbitration_applications  = ArbitrationApplication.objects.filter(case=obj)
        serializer = CaseArbitrationApplicationSerializer(arbitration_applications, many=True)
        return serializer.data
    def get_payments(self, obj):
        payments  = Payment.objects.filter(case=obj)
        serializer = CasePaymentSerializer(payments, many=True)
        return serializer.data

class PaymentSerializer(serializers.ModelSerializer):
    case = CaseSerializer()
    payment_subject = PaymentSubjectSerializer()
    payment_category = PaymentCategorySerializer()
    class Meta:
        model = Payment
        fields = '__all__'

class InsuranceApplicationSerializer(serializers.ModelSerializer):
    case = CaseSerializer()
    class Meta:
        model = InsuranceApplication
        fields = '__all__'

class ArbitrationApplicationSerializer(serializers.ModelSerializer):
    case = CaseSerializer()
    insurance_application = InsuranceApplicationSerializer()
    class Meta:
        model = ArbitrationApplication
        fields = '__all__'
class TotalStatisticsSerializer(serializers.ModelSerializer):
    CaseStatistics.update_statistics()
    # genel_toplam_vekalet_sayisi = serializers.IntegerField(source='total_power_of_attorney_files')
    # aylik_toplam_vekalet_sayisi = serializers.IntegerField(source='total_monthly_power_of_attorney_files')
    # genel_toplam_dosya_sayisi = serializers.IntegerField(source='total_files')
    # aylik_toplam_dosya_sayisi = serializers.IntegerField(source='total_monthly_files')
    # islemsiz_dosyalar = serializers.IntegerField(source='total_unclosed_files_without_insurance_application')
    # sigorta_basvurusu_bekleyen = serializers.IntegerField(source='total_insurance_application_pending_files')
    # sigorta_basvurusu_yapilan = serializers.IntegerField(source='total_insurance_application_files')
    # sigorta_basvurusu_gecikmede = serializers.IntegerField(source='total_delayed_insurance_application_files')
    # tahkim_basvurusu_yapilan = serializers.IntegerField(source='total_arbitration_application_files')
    # tahkim_basvurusu_gecikmede = serializers.IntegerField(source='total_delayed_arbitration_application_files')
    # sahsa_icra = serializers.IntegerField(source='total_personal_lien_files')
    # yalnizca_sigorta_basvurusu = serializers.IntegerField(source='total_files_without_arbitration_application')
    # islemi_biten_odeme_bekleyen = serializers.IntegerField(source='total_payment_pending_files')
    # kapanan_dosyalar = serializers.IntegerField(source='total_closed_files')
    # on_odemeli_islemi_devam_eden = serializers.IntegerField(source='total_pre_payment_files')
    # arti_butce_kapanan = serializers.IntegerField(source='total_profitable_closed_files')
    # eksi_butce_kapanan = serializers.IntegerField(source='total_unprofitable_closed_files')

    class Meta:
        model = CaseStatistics
        fields = '__all__'

# class TotalsSerializer(serializers.Serializer):
#     genel_toplam_vekalet_sayisi = serializers.IntegerField()
#     aylik_toplam_vekalet_sayisi = serializers.IntegerField()
#     genel_toplam_dosya_sayisi = serializers.IntegerField()
#     aylik_toplam_dosya_sayisi = serializers.IntegerField()
#     islemsiz_dosyalar = serializers.IntegerField()
#     sigorta_basvurusu_bekleyen = serializers.IntegerField()
#     sigorta_basvurusu_yapilan = serializers.IntegerField()
#     sigorta_basvurusu_gecikmede = serializers.IntegerField()
#     tahkim_basvurusu_yapilan = serializers.IntegerField()
#     tahkim_basvurusu_gecikmede = serializers.IntegerField()
#     sahsa_icra = serializers.IntegerField()
#     yalnizca_sigorta_basvurusu = serializers.IntegerField()
#     islemi_biten_odeme_bekleyen = serializers.IntegerField()
#     kapanan_dosyalar = serializers.IntegerField()
#     on_odemeli_islemi_devam_eden = serializers.IntegerField()
#     arti_butce_kapanan = serializers.IntegerField()
#     eksi_butce_kapanan = serializers.IntegerField()
#     latency_on_insurance_application = serializers.BooleanField()
#     latency_on_arbitration_application = serializers.BooleanField()