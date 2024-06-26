# Generated by Django 5.0.3 on 2024-04-27 12:34

import django.db.models.deletion
import filemanagement.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leadmanagement', '0002_alter_lead_alternate_phone_alter_lead_created_by_and_more'),
        ('staffmanagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Dava Konusu')),
                ('distraint', models.BooleanField(default=False, verbose_name='İcra Konusu')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Zamanı')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olusturulan_dava_konulari', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan')),
                ('last_updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='son_guncellenen_dava_konulari', to=settings.AUTH_USER_MODEL, verbose_name='Son Güncelleyen')),
            ],
            options={
                'verbose_name': 'Dava',
                'verbose_name_plural': 'Davalar',
            },
        ),
        migrations.CreateModel(
            name='Dosyalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_id', filemanagement.models.CustomBuroNoField(max_length=7, unique=True, verbose_name='Büro No')),
                ('accident_date', models.DateField(verbose_name='Kaza Tarihi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Zamanı')),
                ('case_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filemanagement.casesubject', verbose_name='Dava Konusu')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olusturulan_dosyalar', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan')),
                ('expert_representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffmanagement.expertstaff', verbose_name='Usta/Servis')),
                ('field_representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffmanagement.fieldstaff', verbose_name='Saha Ekibi')),
                ('last_updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='son_guncellenen_dosyalar', to=settings.AUTH_USER_MODEL, verbose_name='Son Güncelleyen')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leadmanagement.lead', verbose_name='Müvekkil')),
                ('office_representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffmanagement.officestaff', verbose_name='Ofis Sorumlusu')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leadmanagement.vehicle', verbose_name='Araç')),
            ],
            options={
                'verbose_name': 'Dosya',
                'verbose_name_plural': 'Dosyalar',
            },
        ),
        migrations.CreateModel(
            name='ArbitrationApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arbitration_id', models.TextField(verbose_name='Esas No')),
                ('arbitration_application_date', models.DateField(verbose_name='Tahkim Başvuru Tarihi')),
                ('arbitration_application_status', models.CharField(blank=True, max_length=100, verbose_name='Tahkim Başvuru Durumu')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Zamanı')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olusturulan_tahkim_basvurulari', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan')),
                ('last_updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='son_guncellenen_tahkim_basvurulari', to=settings.AUTH_USER_MODEL, verbose_name='Son Güncelleyen')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filemanagement.dosyalar', verbose_name='Dosya')),
            ],
            options={
                'verbose_name': 'Tahkim Başvurusu',
                'verbose_name_plural': 'Tahkim Başvuruları',
            },
        ),
        migrations.CreateModel(
            name='InsuranceApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_application_date', models.DateField(verbose_name='Sigorta Başvuru Tarihi')),
                ('insurance_application_status', models.CharField(max_length=100, verbose_name='Sigorta Başvuru Durumu')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Zamanı')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filemanagement.dosyalar', verbose_name='Dosya')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olusturulan_sigorta_basvurulari', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan')),
                ('last_updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='son_guncellenen_sigorta_basvurulari', to=settings.AUTH_USER_MODEL, verbose_name='Son Güncelleyen')),
            ],
            options={
                'verbose_name': 'Sigorta Başvurusu',
                'verbose_name_plural': 'Sigorta Başvuruları',
            },
        ),
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_company_name', models.CharField(max_length=100, unique=True, verbose_name='Sigorta Şirketi Adı')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Zamanı')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olusturulan_sigorta_sirketleri', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan')),
                ('last_updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='son_guncellenen_sigorta_sirketleri', to=settings.AUTH_USER_MODEL, verbose_name='Son Güncelleyen')),
            ],
            options={
                'verbose_name': 'Sigorta Şirketi',
                'verbose_name_plural': 'Sigorta Şirketleri',
            },
        ),
        migrations.AddField(
            model_name='dosyalar',
            name='insurance_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filemanagement.insurancecompany', verbose_name='Sigorta Şirketi'),
        ),
        migrations.CreateModel(
            name='InsuranceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_type', models.CharField(max_length=100, unique=True, verbose_name='Sigorta Türü')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Zamanı')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olusturulan_sigorta_turleri', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan')),
                ('last_updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='son_guncellenen_sigorta_turleri', to=settings.AUTH_USER_MODEL, verbose_name='Son Güncelleyen')),
            ],
            options={
                'verbose_name': 'Sigorta Türü',
                'verbose_name_plural': 'Sigorta Türleri',
            },
        ),
        migrations.AddField(
            model_name='dosyalar',
            name='insurance_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filemanagement.insurancetype', verbose_name='Sigorta Türü'),
        ),
    ]
