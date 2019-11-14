# Generated by Django 2.2.4 on 2019-08-24 13:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Descriçao'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='workload',
            field=models.IntegerField(default=4, verbose_name='Carga horária'),
        ),
        migrations.AlterField(
            model_name='activitytime',
            name='date_end',
            field=models.TimeField(verbose_name='Hora de fim'),
        ),
        migrations.AlterField(
            model_name='activitytime',
            name='date_start',
            field=models.TimeField(verbose_name='Hora de inicio'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='organizers',
            field=models.ManyToManyField(blank=True, related_name='editions', to=settings.AUTH_USER_MODEL, verbose_name='Organizadores'),
        ),
    ]