# Generated by Django 4.1.2 on 2022-12-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Policlinic', '0021_alter_appointment_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='insurance',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='payment',
            field=models.CharField(max_length=100),
        ),
    ]
