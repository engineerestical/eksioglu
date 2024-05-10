from django.db import models
from django.utils import timezone
from filemanagement.models import Case

class CaseStatistics(models.Model):
    total_power_of_attorney_files = models.IntegerField(default=0)
    total_monthly_power_of_attorney_files = models.IntegerField(default=0)
    total_files = models.IntegerField(default=0)
    total_monthly_files = models.IntegerField(default=0)
    total_unclosed_files_without_insurance_application = models.IntegerField(default=0)
    total_insurance_application_pending_files = models.IntegerField(default=0)
    total_insurance_application_files = models.IntegerField(default=0)
    total_delayed_insurance_application_files = models.IntegerField(default=0)
    total_arbitration_application_files = models.IntegerField(default=0)
    total_delayed_arbitration_application_files = models.IntegerField(default=0)
    total_personal_lien_files = models.IntegerField(default=0)
    total_files_without_arbitration_application = models.IntegerField(default=0)
    total_payment_pending_files = models.IntegerField(default=0)
    total_closed_files = models.IntegerField(default=0)
    total_pre_payment_files = models.IntegerField(default=0)
    total_profitable_closed_files = models.IntegerField(default=0)
    total_unprofitable_closed_files = models.IntegerField(default=0)

    @classmethod
    def update_statistics(cls):
        """
        Update the statistics based on the current state of Case objects.
        """
        now = timezone.now()

        # Fetch all Case objects
        all_cases = Case.objects.all()

        # Filter cases based on the is_power_of_attorney_file property
        power_of_attorney_cases = [case for case in all_cases if case.is_power_of_attorney_file]

        # Calculate counts
        cls.total_power_of_attorney_files = len(power_of_attorney_cases)
        cls.total_monthly_power_of_attorney_files = sum(1 for case in power_of_attorney_cases if case.created_at.month == now.month)
        cls.total_files = len(all_cases)
        cls.total_monthly_files = sum(1 for case in all_cases if case.created_at.month == now.month)
        cls.total_unclosed_files_without_insurance_application = sum(1 for case in all_cases if not case.is_closed and not case.insurance_application_date)

        cls.total_insurance_application_pending_files = sum(1 for case in all_cases if case.be_subject_to_insurance_application and not case.insurance_application_date)
        cls.total_insurance_application_files = sum(1 for case in all_cases if case.insurance_application_date)
        cls.total_delayed_insurance_application_files = sum(1 for case in all_cases if case.insurance_application_date and case.insurance_application_date < now.date())
        cls.total_arbitration_application_files = sum(1 for case in all_cases if case.arbitration_application_date)
        cls.total_delayed_arbitration_application_files = sum(1 for case in all_cases if case.arbitration_application_date and case.arbitration_application_date < now.date())
        cls.total_personal_lien_files = sum(1 for case in all_cases if case.is_personel_lien)
        cls.total_files_without_arbitration_application = sum(1 for case in all_cases if case.be_subject_to_arbitration_application and not case.arbitration_application_date and not case.is_closed)
        cls.total_payment_pending_files = sum(1 for case in all_cases if case.is_waiting_payment)
        cls.total_closed_files = sum(1 for case in all_cases if case.is_closed)
        cls.total_pre_payment_files = sum(1 for case in all_cases if case.have_pre_payment and not case.is_closed)
        cls.total_profitable_closed_files = sum(1 for case in all_cases if case.is_closed and case.profit_quantity > 0)
        cls.total_unprofitable_closed_files = sum(1 for case in all_cases if case.is_closed and case.profit_quantity < 0)

        # Get or create the statistics object
        statistics, _ = cls.objects.get_or_create(pk=1)

        # Update counts
        statistics.total_power_of_attorney_files = cls.total_power_of_attorney_files
        statistics.total_monthly_power_of_attorney_files = cls.total_monthly_power_of_attorney_files
        statistics.total_files = cls.total_files
        statistics.total_monthly_files = cls.total_monthly_files
        statistics.total_unclosed_files_without_insurance_application = cls.total_unclosed_files_without_insurance_application
        statistics.total_insurance_application_pending_files = cls.total_insurance_application_pending_files
        statistics.total_insurance_application_files = cls.total_insurance_application_files
        statistics.total_delayed_insurance_application_files = cls.total_delayed_insurance_application_files
        statistics.total_arbitration_application_files = cls.total_arbitration_application_files
        statistics.total_delayed_arbitration_application_files = cls.total_delayed_arbitration_application_files
        statistics.total_personal_lien_files = cls.total_personal_lien_files
        statistics.total_files_without_arbitration_application = cls.total_files_without_arbitration_application
        statistics.total_payment_pending_files = cls.total_payment_pending_files
        statistics.total_closed_files = cls.total_closed_files
        statistics.total_pre_payment_files = cls.total_pre_payment_files
        statistics.total_profitable_closed_files = cls.total_profitable_closed_files
        statistics.total_unprofitable_closed_files = cls.total_unprofitable_closed_files

        # Save changes
        statistics.save()

    def save(self, *args, **kwargs):
        # Ensure only one instance of CaseStatistics exists
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return "Case Statistics"
