# Generated by Django 5.1.2 on 2024-10-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadside_app', '0005_alter_servicetype_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
