# Generated by Django 5.1.2 on 2024-10-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadside_app', '0011_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='location',
            field=models.CharField(max_length=255),
        ),
    ]
