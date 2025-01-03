# Generated by Django 5.1.4 on 2024-12-25 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=32)),
                ('adresse', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Monface.person')),
                ('office', models.CharField(max_length=32)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monface.campus')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monface.job')),
            ],
            bases=('Monface.person',),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_publication', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monface.person')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Monface.person')),
                ('annee', models.IntegerField()),
                ('cursus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monface.cursus')),
            ],
            bases=('Monface.person',),
        ),
    ]
