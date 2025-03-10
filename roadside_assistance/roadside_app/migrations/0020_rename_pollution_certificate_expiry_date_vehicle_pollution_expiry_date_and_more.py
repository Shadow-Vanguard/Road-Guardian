# Generated by Django 5.1.4 on 2025-01-14 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadside_app', '0019_vehicle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='pollution_certificate_expiry_date',
            new_name='pollution_expiry_date',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='pollution_certificate_issue_date',
            new_name='tax_expiry_date',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='insurance_policy_number',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='insurance_provider',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='road_tax_expiry_date',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='road_tax_document',
            field=models.FileField(blank=True, null=True, upload_to='documents/tax/'),
        ),
    ]
