# Generated by Django 5.0.1 on 2024-02-02 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjetPerdu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_signalement', models.DateTimeField(auto_now_add=True)),
                ('lieu_trouve', models.CharField(max_length=255)),
                ('nom_visiteur', models.CharField(max_length=100)),
                ('coordonnees', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/objets_perdus/')),
            ],
        ),
        migrations.CreateModel(
            name='ObjetVole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signale_par', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('date_signalement', models.DateTimeField(auto_now_add=True)),
                ('objet_perdu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mejbour.objetperdu')),
            ],
        ),
    ]