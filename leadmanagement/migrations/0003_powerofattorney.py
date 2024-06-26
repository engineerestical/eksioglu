# Generated by Django 5.0.3 on 2024-04-29 08:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadmanagement', '0002_alter_lead_alternate_phone_alter_lead_created_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PowerOfAttorney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_of_attorney_startdate', models.DateField(verbose_name='Vekalet Başlangıç Tarihi')),
                ('power_of_attorney_enddate', models.DateField(verbose_name='Vekalet Bitiş Tarihi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme Zamanı')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olusturulan_vekaletler', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan')),
                ('last_updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='son_guncellenen_vekaletler', to=settings.AUTH_USER_MODEL, verbose_name='Son Güncelleyen')),
                ('lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leadmanagement.lead', verbose_name='Müvekkil')),
            ],
            options={
                'verbose_name': 'Vekalet',
                'verbose_name_plural': 'Vekaletler',
            },
        ),
    ]
