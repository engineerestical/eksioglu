# utils.py

from django.db.models import Sum
from accountingmanagement.models import Payment

def calculate_profit(case_id):
    # Importing inside the function to avoid circular import
    from filemanagement.models import Case  
    case = Case.objects.get(pk=case_id)
    income_total = Payment.objects.filter(case=case, payment_type='I').aggregate(total=Sum('payment_amount'))['total'] or 0
    outcome_total = Payment.objects.filter(case=case, payment_type='O').aggregate(total=Sum('payment_amount'))['total'] or 0
    return income_total - outcome_total
