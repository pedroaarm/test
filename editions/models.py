# -*- coding: utf-8 -*-
import re
import uuid
from django.db import models
from django.core import validators
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from accounts.models import User
from accounts.models import AuditModel
from django.urls import reverse 
from datetime import date
from django.utils import timezone

class Campus(AuditModel):
	
	name = models.CharField('Campus', max_length=100, blank=False, null=False)

	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('editions:list_campus')

class TypeActivity(AuditModel):
	
	name = models.CharField('Tipo de Atividade', max_length=100, blank=False, null=False)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('editions:list_type_activity')

class Location(AuditModel):
	
	name = models.CharField('Local', max_length=100, blank=False, null=False)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('editions:list_location')
 
class Edition(AuditModel):

	date_start = models.DateTimeField("Data de Inicio das Inscrições na Edição")
	date_end = models.DateTimeField("Data de Fim das Inscrições na  Edição")
	ativo = models.BooleanField('Ativo ' , default=True,blank=False, null=False)
	edition = models.CharField("Adicione Um Nome Para Esta Edição",max_length=100,blank=False, null=False)
	start_of_registrations = models.DateField("Inicio das Incrições Em Atividades" , blank=False, null=False)
	end_of_registrations = models.DateField("Fim das Incrições Em Atividades" , blank=False, null=False)
	organizers = models.ManyToManyField(User,related_name='editions', verbose_name='Organizadores', blank=True)
	qtd_max_authors = models.IntegerField('Quantide máxima de autores', default=1)
	campus = models.ManyToManyField(Campus , verbose_name="Campus ", related_name='campus',blank=True)
	start_submissions = models.DateField("Inicio das Submissões de Trabalhos" , blank=True, null=True)
	end_submissions= models.DateField("Fim das Submissões de Trabalhos" , blank=True, null=True)

	def __str__(self):
		return self.edition

	def get_absolute_url(self):
		return reverse('editions:list_edition')
	def get_campus(self):
		return str(self.campus)


class Inscription(AuditModel):
	status = models.BooleanField('Status da inscrição' , default=False,blank=False, null=False)
	date_of_inscription = models.DateTimeField('Data de Inscrição',blank=False, null=False)
	user = models.ForeignKey('accounts.User' , verbose_name="Usuario", null=True, blank=True , on_delete=models.CASCADE)
	edition = models.ForeignKey('Edition' , verbose_name="Edicao", null=True, blank=True , on_delete=models.CASCADE)
	present = models.BooleanField('Presente ' , default=False,blank=False, null=False)
	campus = models.ForeignKey('Campus' , verbose_name="Campus ", null=True, blank=True ,  on_delete=models.CASCADE)
	def __str__(self):
		return self.status


	def get_absolute_url(self):
		return reverse('editions:list_inscription')
	
class InscriptionActivity(AuditModel):
	status = models.BooleanField('Status da inscrição' , default=False,blank=False, null=False)
	date_of_inscription = models.DateTimeField('Data de Inscrição',blank=False, null=False)
	participant = models.ForeignKey('accounts.User' , verbose_name="Participante", null=True, blank=True,on_delete=models.CASCADE)
	activity = models.ForeignKey('Activity' , verbose_name="Atividade", null=True, blank=True,on_delete=models.CASCADE)
	present = models.BooleanField('Presente ' , default=False,blank=False, null=False)
	inscription = models.ForeignKey('Inscription' , verbose_name="Atividade", null=True, blank=True,on_delete=models.CASCADE)
	 
	def __int__(self): 
		return self.participant

	def get_absolute_url(self):
		return reverse('editions:list_inscription_activity')

class Activity(AuditModel):
		title = models.CharField("Título",max_length=100,blank=False, null=False)
		type_of_activity = models.ForeignKey('TypeActivity' , verbose_name="Tipo de atividade", null=True, blank=True,on_delete=models.CASCADE)
		professional = models.CharField("Profissional",max_length=100,blank=False, null=False)
		vacancies = models.IntegerField('Vagas', default=1)
		workload = models.IntegerField('Carga horária', default=4)
		description = models.TextField("Descriçao",max_length=500,blank=False, null=False)
		edition = models.ForeignKey('Edition' , verbose_name="Edição", null=True, blank=True,on_delete=models.CASCADE)
		location = models.ForeignKey('Location' , verbose_name="lugar", null=True, blank=True,on_delete=models.CASCADE)
		campus = models.ForeignKey('Campus' , verbose_name="Campus ", null=True, blank=True ,  on_delete=models.CASCADE)
		def __str__(self):
			return self.title

		def get_absolute_url(self):
			return reverse('editions:list_activity')

class ActivityTime(AuditModel):
		date_start = models.TimeField('Hora de inicio',blank=False, null=False)
		date_end = models.TimeField('Hora de fim',blank=False, null=False)
		activity = models.ForeignKey('Activity' , verbose_name="Atividade", null=True, blank=True,on_delete=models.CASCADE)
		date = models.DateField('Data',blank=False, null=False)

		def __int__(self):
			return self.activity

		def get_absolute_url(self):
			return reverse('editions:list_activity_time')