from django.urls import path
from .views import (
    ArbitrationApplicationListCreate, ArbitrationApplicationRetrieveUpdateDestroy, CaseListCreate, CaseRetrieveUpdateDestroy, CaseSubjectListCreate, CaseSubjectRetrieveUpdateDestroy, InsuranceApplicationListCreate, InsuranceApplicationRetrieveUpdateDestroy, InsuranceCompanyListCreate, InsuranceCompanyRetrieveUpdateDestroy, InsuranceTypeListCreate, InsuranceTypeRetrieveUpdateDestroy, LeadListCreate, LeadRetrieveUpdateDestroy, PaymentCategoryListCreate, PaymentCategoryRetrieveUpdateDestroy, TotalsListAPIView,
    VehicleListCreate, VehicleRetrieveUpdateDestroy,
    PowerOfAttorneyListCreate, PowerOfAttorneyRetrieveUpdateDestroy,
    PaymentSubjectListCreate, PaymentSubjectRetrieveUpdateDestroy,
    PaymentListCreate, PaymentRetrieveUpdateDestroy,
    DepartmentListCreate, DepartmentRetrieveUpdateDestroy,
    RegionListCreate, RegionRetrieveUpdateDestroy,
    OfficeStaffListCreate, OfficeStaffRetrieveUpdateDestroy,
    ExpertStaffListCreate, ExpertStaffRetrieveUpdateDestroy,
    FieldStaffListCreate, FieldStaffRetrieveUpdateDestroy,
    LatencyOnInsuranceApplicationList, LatencyOnArbitrationApplicationList,
    PowerOfAttorneyFileList, ClosedWithPrePaymentList,
    ClosedList, OpenList, WaitingPaymentList
)

from .api_docs import schema_view

urlpatterns = [
    path('leads/', LeadListCreate.as_view(), name='lead-list-create'),
    path('leads/<int:pk>/', LeadRetrieveUpdateDestroy.as_view(), name='lead-retrieve-update-destroy'),
    path('vehicles/', VehicleListCreate.as_view(), name='vehicle-list-create'),
    path('vehicles/<int:pk>/', VehicleRetrieveUpdateDestroy.as_view(), name='vehicle-retrieve-update-destroy'),
    path('powerofattorneys/', PowerOfAttorneyListCreate.as_view(), name='powerofattorney-list-create'),
    path('powerofattorneys/<int:pk>/', PowerOfAttorneyRetrieveUpdateDestroy.as_view(), name='powerofattorney-retrieve-update-destroy'),
    path('paymentsubjects/', PaymentSubjectListCreate.as_view(), name='paymentsubject-list-create'),
    path('paymentsubjects/<int:pk>/', PaymentSubjectRetrieveUpdateDestroy.as_view(), name='paymentsubject-retrieve-update-destroy'),
    path('paymentcategories/', PaymentCategoryListCreate.as_view(), name='paymentcategories-list-create'),
    path('paymentcategories/<int:pk>/', PaymentCategoryRetrieveUpdateDestroy.as_view(), name='paymentcategories-retrieve-update-destroy'),

    path('payments/', PaymentListCreate.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroy.as_view(), name='payment-retrieve-update-destroy'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # URLs for Insurance Company
    path('insurance-companies/', InsuranceCompanyListCreate.as_view(), name='insurance-company-list-create'),
    path('insurance-companies/<int:pk>/', InsuranceCompanyRetrieveUpdateDestroy.as_view(), name='insurance-company-retrieve-update-destroy'),

    # URLs for Case Subject
    path('case-subjects/', CaseSubjectListCreate.as_view(), name='case-subject-list-create'),
    path('case-subjects/<int:pk>/', CaseSubjectRetrieveUpdateDestroy.as_view(), name='case-subject-retrieve-update-destroy'),

    # URLs for Insurance Type
    path('insurance-types/', InsuranceTypeListCreate.as_view(), name='insurance-type-list-create'),
    path('insurance-types/<int:pk>/', InsuranceTypeRetrieveUpdateDestroy.as_view(), name='insurance-type-retrieve-update-destroy'),

    # URLs for Case
    path('cases/', CaseListCreate.as_view(), name='case-list-create'),
    path('cases/<int:pk>/', CaseRetrieveUpdateDestroy.as_view(), name='case-retrieve-update-destroy'),

    # URLs for Insurance Application
    path('insurance-applications/', InsuranceApplicationListCreate.as_view(), name='insurance-application-list-create'),
    path('insurance-applications/<int:pk>/', InsuranceApplicationRetrieveUpdateDestroy.as_view(), name='insurance-application-retrieve-update-destroy'),

    # URLs for Arbitration Application
    path('arbitration-applications/', ArbitrationApplicationListCreate.as_view(), name='arbitration-application-list-create'),
    path('arbitration-applications/<int:pk>/', ArbitrationApplicationRetrieveUpdateDestroy.as_view(), name='arbitration-application-retrieve-update-destroy'),

    # URLs for Department
    path('departments/', DepartmentListCreate.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroy.as_view(), name='department-detail'),
    
    # URLs for Region
    path('regions/', RegionListCreate.as_view(), name='region-list'),
    path('regions/<int:pk>/', RegionRetrieveUpdateDestroy.as_view(), name='region-detail'),
    
    # URLs for Office Staff
    path('office-staff/', OfficeStaffListCreate.as_view(), name='office-staff-list'),
    path('office-staff/<int:pk>/', OfficeStaffRetrieveUpdateDestroy.as_view(), name='office-staff-detail'),
    
    # URLs for Expert Staff
    path('expert-staff/', ExpertStaffListCreate.as_view(), name='expert-staff-list'),
    path('expert-staff/<int:pk>/', ExpertStaffRetrieveUpdateDestroy.as_view(), name='expert-staff-detail'),
    
    # URLs for Field Staff
    path('field-staff/', FieldStaffListCreate.as_view(), name='field-staff-list'),
    path('field-staff/<int:pk>/', FieldStaffRetrieveUpdateDestroy.as_view(), name='field-staff-detail'),

    #Latency Insurance
    path('cases/latency-on-insurance-application/', LatencyOnInsuranceApplicationList.as_view(), name='latency-on-insurance-application-list'),

    path('cases/latency-on-arbitration-application/', LatencyOnArbitrationApplicationList.as_view(), name='latency-on-arbitration-application-list'),
    path('cases/power-of-attorney-file/', PowerOfAttorneyFileList.as_view(), name='power-of-attorney-file-list'),
    path('cases/closed-with-pre-payment/', ClosedWithPrePaymentList.as_view(), name='closed-with-pre-payment-list'),
    path('cases/closed/', ClosedList.as_view(), name='closed-list'),
    path('cases/open/', OpenList.as_view(), name='open-list'),
    path('cases/waiting-payment/', WaitingPaymentList.as_view(), name='waiting-payment-list'),
    path('totals/', TotalsListAPIView.as_view(), name='totals-list'),
    
]

