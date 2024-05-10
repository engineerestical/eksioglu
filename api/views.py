from rest_framework import generics
from reportmanagement.models import CaseStatistics
from leadmanagement.models import Lead, Vehicle, PowerOfAttorney
from accountingmanagement.models import PaymentSubject, Payment, PaymentCategory
from filemanagement.models import InsuranceCompany, CaseSubject, InsuranceType, Case, InsuranceApplication, ArbitrationApplication
from staffmanagement.models import Department, Region, OfficeStaff, ExpertStaff, FieldStaff
from .serializers import CaseArbitrationApplicationSerializer, CaseInsuranceApplicationSerializer, CasePaymentSerializer, LeadSerializer, PaymentCategorySerializer, TotalStatisticsSerializer, VehicleSerializer, PowerOfAttorneySerializer, PaymentSubjectSerializer, PaymentSerializer, InsuranceCompanySerializer, CaseSubjectSerializer, InsuranceTypeSerializer, CaseSerializer, InsuranceApplicationSerializer, ArbitrationApplicationSerializer, DepartmentSerializer, RegionSerializer, OfficeStaffSerializer, ExpertStaffSerializer, FieldStaffSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from datetime import datetime, date, timedelta
from django.db.models import F, Q 
from django_property_filter import PropertyFilterSet, PropertyNumberFilter
from django.db.models.functions import TruncDate

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class VehicleListCreate(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class PowerOfAttorneyListCreate(generics.ListCreateAPIView):
    queryset = PowerOfAttorney.objects.all()
    serializer_class = PowerOfAttorneySerializer

class PowerOfAttorneyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PowerOfAttorney.objects.all()
    serializer_class = PowerOfAttorneySerializer

class PaymentSubjectListCreate(generics.ListCreateAPIView):
    queryset = PaymentSubject.objects.all()
    serializer_class = PaymentSubjectSerializer

class PaymentSubjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentSubject.objects.all()
    serializer_class = PaymentSubjectSerializer

class PaymentCategoryListCreate(generics.ListCreateAPIView):
    queryset = PaymentCategory.objects.all()
    serializer_class = PaymentCategorySerializer

class PaymentCategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentCategory.objects.all()
    serializer_class = PaymentCategorySerializer

class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


# Views for Insurance Company
class InsuranceCompanyListCreate(generics.ListCreateAPIView):
    queryset = InsuranceCompany.objects.all()
    serializer_class = InsuranceCompanySerializer

class InsuranceCompanyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsuranceCompany.objects.all()
    serializer_class = InsuranceCompanySerializer

# Views for Case Subject
class CaseSubjectListCreate(generics.ListCreateAPIView):
    queryset = CaseSubject.objects.all()
    serializer_class = CaseSubjectSerializer

class CaseSubjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CaseSubject.objects.all()
    serializer_class = CaseSubjectSerializer

# Views for Insurance Type
class InsuranceTypeListCreate(generics.ListCreateAPIView):
    queryset = InsuranceType.objects.all()
    serializer_class = InsuranceTypeSerializer

class InsuranceTypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsuranceType.objects.all()
    serializer_class = InsuranceTypeSerializer

# Views for Case

class CaseListCreate(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class CaseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

# Views for Insurance Application
class InsuranceApplicationListCreate(generics.ListCreateAPIView):
    queryset = InsuranceApplication.objects.all()
    serializer_class = InsuranceApplicationSerializer

class InsuranceApplicationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = InsuranceApplication.objects.all()
    serializer_class = InsuranceApplicationSerializer

class CaseInsuranceApplicationListCreate(generics.ListCreateAPIView):
    queryset = InsuranceApplication.objects.all()
    serializer_class = CaseInsuranceApplicationSerializer
class CaseArbitrationApplicationListCreate(generics.ListCreateAPIView):
    queryset = ArbitrationApplication.objects.all()
    serializer_class = CaseArbitrationApplicationSerializer
class CasePaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = CasePaymentSerializer


# Views for Arbitration Application
class ArbitrationApplicationListCreate(generics.ListCreateAPIView):
    queryset = ArbitrationApplication.objects.all()
    serializer_class = ArbitrationApplicationSerializer

class ArbitrationApplicationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArbitrationApplication.objects.all()
    serializer_class = ArbitrationApplicationSerializer


# Views for Department
class DepartmentListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# Views for Region
class RegionListCreate(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

# Views for Office Staff
class OfficeStaffListCreate(generics.ListCreateAPIView):
    queryset = OfficeStaff.objects.all()
    serializer_class = OfficeStaffSerializer

class OfficeStaffRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfficeStaff.objects.all()
    serializer_class = OfficeStaffSerializer

# Views for Expert Staff
class ExpertStaffListCreate(generics.ListCreateAPIView):
    queryset = ExpertStaff.objects.all()
    serializer_class = ExpertStaffSerializer

class ExpertStaffRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpertStaff.objects.all()
    serializer_class = ExpertStaffSerializer

# Views for Field Staff
class FieldStaffListCreate(generics.ListCreateAPIView):
    queryset = FieldStaff.objects.all()
    serializer_class = FieldStaffSerializer

class FieldStaffRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FieldStaff.objects.all()
    serializer_class = FieldStaffSerializer


class LatencyOnInsuranceApplicationList(generics.ListAPIView):
    serializer_class = CaseSerializer

    def get_queryset(self):
        """
        Get cases with latency on insurance application.
        """
        queryset = Case.objects.all()

        field_representative = self.request.query_params.get('field_representative')
        if field_representative:
            queryset = queryset.filter(field_representative=field_representative)

        expert_representative = self.request.query_params.get('expert_representative')
        if expert_representative:
            queryset = queryset.filter(expert_representative=expert_representative)

        # Filter cases with latency on insurance application
        queryset = [case for case in queryset if case.latency_on_insurance_application]

        return queryset
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='field_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the field representative.'
            ),
            openapi.Parameter(
                name='expert_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the expert representative.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class LatencyOnArbitrationApplicationList(generics.ListAPIView):
    serializer_class = CaseSerializer

    def get_queryset(self):
        queryset = Case.objects.filter(latency_on_arbitration_application=True)
        field_representative = self.request.query_params.get('field_representative', None)
        expert_representative = self.request.query_params.get('expert_representative', None)
        
        if field_representative:
            queryset = queryset.filter(field_representative=field_representative)
        if expert_representative:
            queryset = queryset.filter(expert_representative=expert_representative)
        
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='field_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the field representative.'
            ),
            openapi.Parameter(
                name='expert_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the expert representative.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PowerOfAttorneyFileList(generics.ListAPIView):
    serializer_class = CaseSerializer

    def get_queryset(self):
        queryset = Case.objects.filter(is_power_of_attorney_file=True)
        field_representative = self.request.query_params.get('field_representative', None)
        expert_representative = self.request.query_params.get('expert_representative', None)
        
        if field_representative:
            queryset = queryset.filter(field_representative=field_representative)
        if expert_representative:
            queryset = queryset.filter(expert_representative=expert_representative)
        
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='field_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the field representative.'
            ),
            openapi.Parameter(
                name='expert_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the expert representative.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ClosedWithPrePaymentList(generics.ListAPIView):
    serializer_class = CaseSerializer

    def get_queryset(self):
        queryset = Case.objects.filter(is_closed_with_pre_payment=True)
        field_representative = self.request.query_params.get('field_representative', None)
        expert_representative = self.request.query_params.get('expert_representative', None)
        
        if field_representative:
            queryset = queryset.filter(field_representative=field_representative)
        if expert_representative:
            queryset = queryset.filter(expert_representative=expert_representative)
        
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='field_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the field representative.'
            ),
            openapi.Parameter(
                name='expert_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the expert representative.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ClosedList(generics.ListAPIView):
    serializer_class = CaseSerializer

    def get_queryset(self):
        queryset = Case.objects.filter(is_closed=True)
        field_representative = self.request.query_params.get('field_representative', None)
        expert_representative = self.request.query_params.get('expert_representative', None)
        
        if field_representative:
            queryset = queryset.filter(field_representative=field_representative)
        if expert_representative:
            queryset = queryset.filter(expert_representative=expert_representative)
        
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='field_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the field representative.'
            ),
            openapi.Parameter(
                name='expert_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the expert representative.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class OpenList(generics.ListAPIView):
    serializer_class = CaseSerializer

    def get_queryset(self):
        queryset = Case.objects.filter(is_closed=False)
        field_representative = self.request.query_params.get('field_representative', None)
        expert_representative = self.request.query_params.get('expert_representative', None)
        
        if field_representative:
            queryset = queryset.filter(field_representative=field_representative)
        if expert_representative:
            queryset = queryset.filter(expert_representative=expert_representative)
        
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='field_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the field representative.'
            ),
            openapi.Parameter(
                name='expert_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the expert representative.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class WaitingPaymentList(generics.ListAPIView):
    serializer_class = CaseSerializer

    def get_queryset(self):
        queryset = Case.objects.filter(is_waiting_payment=True)
        field_representative = self.request.query_params.get('field_representative', None)
        expert_representative = self.request.query_params.get('expert_representative', None)
        
        if field_representative:
            queryset = queryset.filter(field_representative=field_representative)
        if expert_representative:
            queryset = queryset.filter(expert_representative=expert_representative)
        
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='field_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the field representative.'
            ),
            openapi.Parameter(
                name='expert_representative',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description='ID of the expert representative.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class TotalsListAPIView(generics.ListAPIView):
    serializer_class = TotalStatisticsSerializer

    def get_queryset(self):
        # Assuming you have a method in your CaseStatistics model to fetch the aggregated data
        return CaseStatistics.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        # You can add any additional context data here if needed
        return context

# class TotalsListAPIView(generics.ListAPIView):
#     serializer_class = TotalsSerializer

#     def get_queryset(self):
#         return Case.objects.all()

#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         total_cases = self.get_queryset()
#         genel_toplam_vekalet_sayisi = sum(1 for case in total_cases if case.is_power_of_attorney_file)
        
#         # Filter cases based on property
#         # total_cases_with_power_of_attorney = [case for case in total_cases if case.is_power_of_attorney_file]
#         total_cases_this_month = [case for case in total_cases if case.created_at.month == date.today().month]

#         context['genel_toplam_vekalet_sayisi'] = genel_toplam_vekalet_sayisi
#         context['aylik_toplam_vekalet_sayisi'] = sum(1 for case in total_cases_this_month if case.is_power_of_attorney_file)
#         context['genel_toplam_dosya_sayisi'] = total_cases.count()
#         context['aylik_toplam_dosya_sayisi'] = len(total_cases_this_month)
#         context['islemsiz_dosyalar'] = sum(1 for case in total_cases if case.is_closed and not case.insurance_application_date and not case.arbitration_application_date)
#         context['sigorta_basvurusu_bekleyen'] = sum(1 for case in total_cases if case.be_subject_to_insurance_application and not case.insurance_application_date)
#         context['sigorta_basvurusu_yapilan'] = sum(1 for case in total_cases if case.insurance_application_date)
#         context['sigorta_basvurusu_gecikmede'] = total_cases.filter(Q(insurance_application_date__lt=TruncDate(F('created_at'))) | Q(insurance_application_date__isnull=True)).count()
#         context['tahkim_basvurusu_yapilan'] = total_cases.filter(arbitration_application_date__isnull=False).count()
#         context['tahkim_basvurusu_gecikmede'] = total_cases.filter(Q(arbitration_application_date__lt=TruncDate(F('created_at'))) | Q(arbitration_application_date__isnull=True)).count()
#         context['sahsa_icra'] = sum(1 for case in total_cases if case.is_personel_lien)
#         context['yalnizca_sigorta_basvurusu'] = sum(1 for case in total_cases if not case.be_subject_to_arbitration_application and not case.is_closed)
#         context['islemi_biten_odeme_bekleyen'] = sum(1 for case in total_cases if case.is_waiting_payment)
#         context['kapanan_dosyalar'] = sum(1 for case in total_cases if case.is_closed)
#         context['on_odemeli_islemi_devam_eden'] = sum(1 for case in total_cases if case.have_pre_payment and not case.is_closed)
#         context['arti_butce_kapanan'] = sum(1 for case in total_cases if case.is_closed and case.profit_quantity > 0)
#         context['eksi_butce_kapanan'] = sum(1 for case in total_cases if case.is_closed and case.profit_quantity < 0)

#         return context
