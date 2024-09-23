# Generated by Django 5.1 on 2024-09-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadside_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(db_index=True, default='default@example.com', max_length=150),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
