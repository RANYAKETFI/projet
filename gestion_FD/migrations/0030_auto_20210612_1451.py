# Generated by Django 3.2.3 on 2021-06-12 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_FD', '0029_auto_20210609_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='eval_module',
            name='appreciation',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='eval_module',
            name='type',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_deliberation',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 14, 51, 39, 591930)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_inscription',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 14, 51, 39, 591930)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 14, 51, 39, 591930)),
        ),
        migrations.AlterField(
            model_name='doctorant',
            name='date_reinscription',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 14, 51, 39, 591930)),
        ),
        migrations.AlterField(
            model_name='employe',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 14, 51, 39, 586942)),
        ),
        migrations.AlterField(
            model_name='eval_module',
            name='date_eval',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 14, 51, 39, 596916)),
        ),
        migrations.AlterField(
            model_name='fiche_evaluation',
            name='date_eval',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 14, 51, 39, 594921)),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='date_pres',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 14, 51, 39, 593924)),
        ),
        migrations.AlterField(
            model_name='reinscription',
            name='date_reinscription',
            field=models.DateField(default=datetime.datetime(2021, 6, 12, 14, 51, 39, 589935)),
        ),
        migrations.DeleteModel(
            name='PV',
        ),
    ]
