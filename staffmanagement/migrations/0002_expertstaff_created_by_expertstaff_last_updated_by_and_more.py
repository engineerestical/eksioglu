# Generated by Django 5.0.3 on 2024-04-28 17:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffmanagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='expertstaff',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olusturulan_usta_servisler', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan'),
        ),
        migrations.AddField(
            model_name='expertstaff',
            name='last_updated_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='son_guncellenen_usta_servisler', to=settings.AUTH_USER_MODEL, verbose_name='Son Güncelleyen'),
        ),
        migrations.AddField(
            model_name='fieldstaff',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olusturulan_saha_ekipleri', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan'),
        ),
        migrations.AddField(
            model_name='fieldstaff',
            name='last_updated_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='son_guncellenen_saha_ekipleri', to=settings.AUTH_USER_MODEL, verbose_name='Son Güncelleyen'),
        ),
        migrations.AddField(
            model_name='officestaff',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olusturulan_ofis_personeli', to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan'),
        ),
        migrations.AddField(
            model_name='officestaff',
            name='last_updated_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='son_guncellenen_ofis_personeli', to=settings.AUTH_USER_MODEL, verbose_name='Son Güncelleyen'),
        ),
    ]
