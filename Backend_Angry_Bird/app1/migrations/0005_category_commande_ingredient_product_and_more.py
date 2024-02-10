# Generated by Django 4.2.7 on 2024-01-19 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_pastien_dossier_medical_patien_rdv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.category')),
                ('ingredients', models.ManyToManyField(related_name='products', to='app1.ingredient')),
            ],
        ),
        migrations.RemoveField(
            model_name='dossier_medical',
            name='Dpt',
        ),
        migrations.RemoveField(
            model_name='dossier_medical',
            name='patien',
        ),
        migrations.RemoveField(
            model_name='medecin',
            name='Departement',
        ),
        migrations.RemoveField(
            model_name='rdv',
            name='Medecin',
        ),
        migrations.RemoveField(
            model_name='rdv',
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Departement',
        ),
        migrations.DeleteModel(
            name='Dossier_Medical',
        ),
        migrations.DeleteModel(
            name='Medecin',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='RDV',
        ),
        migrations.AddField(
            model_name='commande',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product'),
        ),
    ]