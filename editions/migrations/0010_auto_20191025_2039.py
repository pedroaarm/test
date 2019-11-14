# Generated by Django 2.2.4 on 2019-10-25 23:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0009_auto_20191025_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edition',
            name='end_activity',
        ),
        migrations.RemoveField(
            model_name='edition',
            name='start_activity',
        ),
        migrations.AddField(
            model_name='edition',
            name='end_submissions',
            field=models.DateField(default=datetime.date(2019, 10, 25), verbose_name='Fim das Submissões de Trabalhos'),
        ),
        migrations.AddField(
            model_name='edition',
            name='start_submissions',
            field=models.DateField(default=datetime.date(2019, 10, 25), verbose_name='Inicio das Submissões de Trabalhos'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='edition',
            field=models.CharField(max_length=100, verbose_name='Adicione Um Nome Para Esta Edição'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='end_of_registrations',
            field=models.DateField(verbose_name='Fim das Incrições Em Atividades'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='start_of_registrations',
            field=models.DateField(verbose_name='Inicio das Incrições Em Atividades'),
        ),
    ]