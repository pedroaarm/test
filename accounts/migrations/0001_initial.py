# Generated by Django 2.2.4 on 2019-08-13 19:13

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import easy_thumbnails.fields
import re
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Autalizado em')),
                ('username', models.CharField(default=uuid.uuid4, help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Informe um nome de usuário válido. Este valor deve conter apenas letras, números e os caracteres: @/./+/-/_ .', 'invalid')], verbose_name='Usuário')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Equipe')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('is_superuser', models.BooleanField(default=True, verbose_name='Super-Usuário')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF')),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='F', max_length=1, verbose_name='Sexo')),
                ('phone', models.CharField(blank=True, max_length=16, null=True, verbose_name='Celular')),
                ('is_whatsapp', models.BooleanField(default=False, verbose_name='O celular é WhatsApp?')),
                ('avatar', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='avatar')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
