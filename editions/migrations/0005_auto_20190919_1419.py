# Generated by Django 2.2.4 on 2019-09-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0004_remove_activity_time_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo '),
        ),
    ]
