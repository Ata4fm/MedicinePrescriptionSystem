# Generated by Django 5.1.2 on 2024-10-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_module', '0009_alter_patient_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientHealthyInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=100, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='code',
            field=models.SmallIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='firstname',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lastname',
            field=models.CharField(max_length=100, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phonenumber',
            field=models.IntegerField(verbose_name='شماره تلفن'),
        ),
        migrations.AddField(
            model_name='patient',
            name='information',
            field=models.ManyToManyField(to='patient_module.patienthealthyinformation'),
        ),
    ]
