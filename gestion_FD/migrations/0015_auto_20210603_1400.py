# Generated by Django 3.2.3 on 2021-06-03 13:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion_FD', '0014_auto_20210528_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duree', models.IntegerField()),
                ('type_bourse', models.CharField(choices=[('PNE', 'PNE'), ('PROFAS', 'PROFAS'), ('Autres', 'Autre')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='fiche_evaluation',
            name='Presentation',
        ),
        migrations.RemoveField(
            model_name='module',
            name='evaluation',
        ),
        migrations.RemoveField(
            model_name='these',
            name='doctorant',
        ),
        migrations.AddField(
            model_name='doctorant',
            name='adresse',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='doctorant',
            name='choix',
            field=models.ManyToManyField(to='gestion_FD.These'),
        ),
        migrations.AddField(
            model_name='doctorant',
            name='choixfinal',
            field=models.CharField(default='Pas Encore', max_length=100),
        ),
        migrations.AddField(
            model_name='doctorant',
            name='employeur',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='doctorant',
            name='profession',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='doctorant',
            name='situation_familiale',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='doctorant',
            name='telephone',
            field=models.CharField(default='00', max_length=100),
        ),
        migrations.AddField(
            model_name='employe',
            name='co_tut',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eval_module',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion_FD.module'),
        ),
        migrations.AddField(
            model_name='these',
            name='etab_part',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='compte',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_deliberation',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 14, 0, 31, 330952)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_inscription',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 14, 0, 31, 330952)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 14, 0, 31, 330952)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_reinscription',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 14, 0, 31, 330952)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='dossier',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gestion_FD.dossier_doctorant'),
        ),
        migrations.AlterField(
            model_name='employe',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 14, 0, 31, 327949)),
        ),
        migrations.AlterField(
            model_name='eval_module',
            name='date_eval',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 14, 0, 31, 335939)),
        ),
        migrations.AlterField(
            model_name='fiche_evaluation',
            name='date_eval',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 14, 0, 31, 333943)),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='date_pres',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 14, 0, 31, 332944)),
        ),
        migrations.AlterField(
            model_name='pv',
            name='date_pv',
            field=models.DateField(default=datetime.datetime(2021, 6, 3, 14, 0, 31, 336936)),
        ),
        migrations.AlterField(
            model_name='these',
            name='date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.CreateModel(
            name='Reinscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reinscription', models.DateField(default=datetime.datetime(2021, 6, 3, 14, 0, 31, 329951))),
                ('declaration', models.CharField(choices=[('le doctorant accuse un retard important dans ses travaux', 'le doctorant accuse un retard important dans ses travaux'), ('le doctorant accuse un retard peu important dans ses travaux', 'le doctorant accuse un retard peu important dans ses travaux'), ('les travaux du doctorant avancent conformément à l’échéancier établi', 'les travaux du doctorant avancent conformément à l’échéancier établi')], max_length=100)),
                ('avis', models.BooleanField(default=False)),
                ('dt', models.BooleanField(default=None)),
                ('prof', models.ManyToManyField(to='gestion_FD.Employe')),
            ],
        ),
        migrations.AddField(
            model_name='doctorant',
            name='Bourse',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gestion_FD.bourse'),
        ),
        migrations.AddField(
            model_name='doctorant',
            name='reinscription',
            field=models.ManyToManyField(to='gestion_FD.Reinscription'),
        ),
    ]
