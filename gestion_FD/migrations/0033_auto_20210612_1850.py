# Generated by Django 3.2.3 on 2021-06-12 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_FD', '0032_auto_20210612_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorant',
            name='date_deliberation',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 18, 49, 57, 682386)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_inscription',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 18, 49, 57, 682386)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 18, 49, 57, 682386)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_reinscription',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 18, 49, 57, 682386)),
        ),
        migrations.AlterField(
            model_name='employe',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 18, 49, 57, 682386)),
        ),
        migrations.AlterField(
            model_name='eval_module',
            name='date_eval',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 18, 49, 57, 698011)),
        ),
        migrations.AlterField(
            model_name='fiche_evaluation',
            name='date_eval',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 18, 49, 57, 682386)),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='date_pres',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 18, 49, 57, 682386)),
        ),
        migrations.AlterField(
            model_name='reinscription',
            name='date_reinscription',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 18, 49, 57, 682386)),
        ),
    ]
