# Generated by Django 4.1.2 on 2022-12-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_userprofile_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer', models.CharField(max_length=250)),
                ('status', models.CharField(blank=True, choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
