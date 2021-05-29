# Generated by Django 3.2.3 on 2021-05-28 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_FD', '0013_auto_20210528_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorant',
            name='date_deliberation',
            field=models.DateField(default=datetime.datetime(2021, 5, 28, 15, 50, 45, 836768)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_inscription',
            field=models.DateField(default=datetime.datetime(2021, 5, 28, 15, 50, 45, 836768)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2021, 5, 28, 15, 50, 45, 836768)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_reinscription',
            field=models.DateField(default=datetime.datetime(2021, 5, 28, 15, 50, 45, 836768)),
        ),
        migrations.AlterField(
            model_name='employe',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2021, 5, 28, 15, 50, 45, 837765)),
        ),
        migrations.AlterField(
            model_name='eval_module',
            name='date_eval',
            field=models.DateField(default=datetime.datetime(2021, 5, 28, 15, 50, 45, 842752)),
        ),
        migrations.AlterField(
            model_name='fiche_evaluation',
            name='date_eval',
            field=models.DateField(default=datetime.datetime(2021, 5, 28, 15, 50, 45, 840758)),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='date_pres',
            field=models.DateField(default=datetime.datetime(2021, 5, 28, 15, 50, 45, 839760)),
        ),
        migrations.AlterField(
            model_name='pv',
            name='date_pv',
            field=models.DateField(default=datetime.datetime(2021, 5, 28, 15, 50, 45, 844751)),
        ),
    ]
