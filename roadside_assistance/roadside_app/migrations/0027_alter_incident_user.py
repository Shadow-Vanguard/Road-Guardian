# Generated by Django 5.1.4 on 2025-02-10 04:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadside_app', '0026_incident'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidents', to=settings.AUTH_USER_MODEL),
        ),
    ]
