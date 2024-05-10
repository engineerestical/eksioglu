# Generated by Django 5.0.3 on 2024-05-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanagement', '0007_arbitrationapplication_insurance_application_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='claimed_lost_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Talep Edilen DK Tutarı'),
        ),
        migrations.AddField(
            model_name='case',
            name='closed_at',
            field=models.DateField(blank=True, null=True, verbose_name='Dosya Kapanma Tarihi'),
        ),
    ]