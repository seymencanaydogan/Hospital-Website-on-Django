# Generated by Django 4.1.2 on 2022-12-26 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Policlinic', '0029_alter_randevu_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='randevu',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='randevu',
            name='policlinic',
        ),
    ]
