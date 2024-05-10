# Generated by Django 5.0.3 on 2024-05-08 09:33

import django.db.models.deletion
import filemanagement.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanagement', '0006_alter_casesubject_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='arbitrationapplication',
            name='insurance_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filemanagement.insuranceapplication', verbose_name='Sigorta Başvurusu'),
        ),
        migrations.AddField(
            model_name='case',
            name='insurance_application_id',
            field=filemanagement.models.CustomInsuranceApplicationIDField(blank=True, editable=False, max_length=7, null=True, unique=True, verbose_name='Sigorta Başvuru Ofis No'),
        ),
    ]
