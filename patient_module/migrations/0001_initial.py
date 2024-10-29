# Generated by Django 5.1.2 on 2024-10-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phonenumber', models.IntegerField(max_length=11)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
