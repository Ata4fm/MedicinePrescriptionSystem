# Generated by Django 5.1.2 on 2024-10-27 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_module', '0004_alter_medicine_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='category',
        ),
        migrations.AddField(
            model_name='medicine',
            name='category',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicine_module.medicinecategory', verbose_name='دسته بندی'),
        ),
    ]
