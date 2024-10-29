# Generated by Django 5.1.2 on 2024-10-27 08:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_module', '0008_alter_patient_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='code',
            field=models.SmallIntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
