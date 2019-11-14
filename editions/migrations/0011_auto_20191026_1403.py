# Generated by Django 2.2.4 on 2019-10-26 17:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0010_auto_20191025_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='date_end',
            field=models.DateTimeField(verbose_name='Data de Fim das Inscrições na  Edição'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='date_start',
            field=models.DateTimeField(verbose_name='Data de Inicio das Inscrições na Edição'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='end_submissions',
            field=models.DateField(default=datetime.datetime(2019, 10, 26, 17, 3, 42, 586412, tzinfo=utc), verbose_name='Fim das Submissões de Trabalhos'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='start_submissions',
            field=models.DateField(default=datetime.datetime(2019, 10, 26, 17, 3, 42, 586361, tzinfo=utc), verbose_name='Inicio das Submissões de Trabalhos'),
        ),
    ]
