# Generated by Django 4.2.7 on 2024-01-20 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_departement_dossier_medical_medecin_patient_rdv_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='num_tel',
        ),
        migrations.AddField(
            model_name='patient',
            name='num_tel_patient',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medecin',
            name='num_tel_med',
            field=models.IntegerField(max_length=10),
        ),
    ]