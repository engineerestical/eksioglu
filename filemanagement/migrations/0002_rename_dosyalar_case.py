# Generated by Django 5.0.3 on 2024-04-27 12:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filemanagement', '0001_initial'),
        ('leadmanagement', '0002_alter_lead_alternate_phone_alter_lead_created_by_and_more'),
        ('staffmanagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dosyalar',
            new_name='Case',
        ),
    ]
