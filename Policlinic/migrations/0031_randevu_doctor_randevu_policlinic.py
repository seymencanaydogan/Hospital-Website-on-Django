# Generated by Django 4.1.2 on 2022-12-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Policlinic', '0030_remove_randevu_doctor_remove_randevu_policlinic'),
    ]

    operations = [
        migrations.AddField(
            model_name='randevu',
            name='doctor',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='randevu',
            name='policlinic',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
