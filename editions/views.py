from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.db import IntegrityError, transaction
from django.contrib import messages
from dal import autocomplete
from .models import Campus
from django.contrib.auth.decorators import login_required
from .forms import*
from accounts.models import User
from datetime import datetime , date
# <<<<<<< HEAD
from datetime import datetime
# =======
# >>>>>>> development
from django.views.generic import View

class CreateCampus(CreateView): 
	model = Campus
	form_class = CampusForm
	template_name = 'campus/add.html'

class UpdateCampus(UpdateView):
	model = Campus
	form_class = CampusForm
	template_name = 'campus/add.html'

def campus_delete(request, pk):
	campus= get_object_or_404(Campus, pk=pk)
	campus.delete()
	return JsonResponse({'msg': "Campus excluido com sucesso!", 'code': "1"})

class ListCampus(ListView):

	model = Campus
	http_method_names = ['get']
	template_name = 'campus/list.html'
	context_object_name = 'campus'
	paginate_by = 25

	def get_queryset(self):
		self.queryset = super(ListCampus, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter(name__icontains = self.request.GET['search_box'])
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(ListCampus, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
		    startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
		    endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]
		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
		    })
		return context


# TypeActivity
class CreateTypeActivity(CreateView):
	model = TypeActivity
	form_class = TypeActivityForm
	template_name = 'typeactivity/add.html'

class UpdateTypeActivity(UpdateView):
	model = TypeActivity
	form_class = TypeActivityForm
	template_name = 'typeactivity/add.html'


def typeactivity_delete(request, pk):
	typeactivity= get_object_or_404(TypeActivity, pk=pk)
	typeactivity.delete()
	return JsonResponse({'msg': "Atividade excluida com sucesso!", 'code': "1"})

class ListTypeActivity(ListView):

	model = TypeActivity
	http_method_names = ['get']
	template_name = 'typeactivity/list.html'
	context_object_name = 'typeactivity'
	paginate_by = 25

	def get_queryset(self):
		self.queryset = super(ListTypeActivity, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter(name__icontains = self.request.GET['search_box'])
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(ListTypeActivity, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
		    startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
		    endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]
		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
		    })
		return context

# Location

class CreateLocation(CreateView):
	model = Location
	form_class = LocationForm
	template_name = 'location/add.html'

class UpdateLocation(UpdateView):
	model = Location
	form_class = LocationForm
	template_name = 'location/add.html'

def location_delete(request, pk):
	location= get_object_or_404(Location, pk=pk)
	location.delete()
	return JsonResponse({'msg': "Lugar excluido com sucesso!", 'code': "1"})

class ListLocation(ListView):

	model = Location
	http_method_names = ['get']
	template_name = 'location/list.html'
	context_object_name = 'location'
	paginate_by = 25

	def get_queryset(self):
		self.queryset = super(ListLocation, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter(name__icontains = self.request.GET['search_box'])
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(ListLocation, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
		    startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
		    endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]
		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
		    })
		return context

# Edition
class CreateEdition(CreateView):
	model = Edition
	form_class = EditionForm
	template_name = 'edition/add.html'

	def post(self, request, *args, **kwargs):
		self.object = None
		
		form = self.form_class(self.request.POST)

		if form.is_valid():
			return self.form_valid(form, request)

		else:
			return self.form_invalid(form, request)

	def form_valid(self, form , request):

		self.object = form.save()
		
		all_editions = Edition.objects.all() 
		for editionItem in all_editions:
			object_edition = get_object_or_404(Edition,id=editionItem.id)
			print(object_edition.ativo)
			if object_edition.ativo == True:
				object_edition.ativo = False
				object_edition.save()

		self.object.save()

		# form.save_m2m()
		
		return HttpResponseRedirect(reverse('editions:list_edition'))

class UpdateEdition(UpdateView):
	model = Edition
	form_class = EditionForm
	template_name = 'edition/add.html'

class DetailEdition(DetailView):
	model = Edition
	template_name = 'edition/detail.html'

def edition_delete(request, pk):
	edition= get_object_or_404(Edition, pk=pk)
	edition.delete()
	return JsonResponse({'msg': "Edição excluido com sucesso!", 'code': "1"})

class ListEdition(ListView):

	model = Edition
	http_method_names = ['get']
	template_name = 'edition/list.html'
	context_object_name = 'edition'
	paginate_by = 25

	def get_queryset(self):
		self.queryset = super(ListEdition, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter( edition__icontains = self.request.GET['search_box']) 
		return self.queryset

	def get_context_data(self, **kwargs):
		
		_super = super(ListEdition, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
		    startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
		    endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]
		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
		    })
		return context

# Inscription For admin
class CreateInscription(CreateView):
	model = Inscription
	form_class = InscriptionForm
	template_name = 'inscription/add.html'

	def post(self, request, *args, **kwargs):
		self.object = None
		
		form = self.form_class(self.request.POST)

		if form.is_valid():
			return self.form_valid(form, request)

		else:
			return self.form_invalid(form, request)

	def form_valid(self, form , request):
		
		inscription = form.save(commit=False)

		
		inscription.date_of_inscription = datetime.now()
		inscription.edition = Edition.objects.filter(start_of_registrations__lte=datetime.now() , end_of_registrations__gte=datetime.now(),campus=inscription.campus ).first()
		
		if Inscription.objects.filter(user=inscription.user).count() > 0:
			messages.error(self.request, 'Este participante já está inscrito nesta edição.')
			return HttpResponseRedirect(reverse('editions:add_inscription'))			
		if not inscription.edition:
			messages.warning(self.request, 'Houve um erro ao tentar cadastrar este participante. Verifique se o campus faz parte da edição.')
			return HttpResponseRedirect(reverse('editions:add_inscription'))
		else:
			inscription.save()
			return HttpResponseRedirect(reverse('editions:list_inscription'))


class UpdateInscription(UpdateView):
	model = Inscription
	form_class = InscriptionForm
	template_name = 'inscription/add.html'

def inscription_delete(request, pk):
	inscription= get_object_or_404(Inscription, pk=pk)
	inscription.delete()
	return JsonResponse({'msg': "Inscrição excluido com sucesso!", 'code': "1"})

class ListInscription(ListView):

	model = Inscription
	http_method_names = ['get']
	template_name = 'inscription/list.html'
	context_object_name = 'inscription'
	paginate_by = 25

	def get_queryset(self):
		self.queryset = super(ListInscription, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter(Q(user__name__icontains = self.request.GET['search_box']) | Q(campus__name__icontains = self.request.GET['search_box'])) 
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(ListInscription, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
		    startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
		    endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]
		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
		    })
		return context



# Activity

class CreateActivity(CreateView):
	model = Activity
	form_class = ActivityForm
	template_name = 'activity/add.html'


	def get(self, request, *args, **kwargs):
		self.object = None
		form = self.form_class

		self.activity_time_formset = ActivityTimeFormSet()
		return self.render_to_response(
			self.get_context_data(
           		form=form,
	            activity_time_formset=self.activity_time_formset
	        )
	    )

	def post(self, request, *args, **kwargs):
		self.object = None
		form = self.form_class(self.request.POST, self.request.FILES)
		self.activity_time_formset = ActivityTimeFormSet(self.request.POST)
		if form.is_valid() and self.activity_time_formset.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):

		try:
			with transaction.atomic():
				self.object = form.save()
				self.activity_time_formset.instance = self.object
				self.activity_time_formset.save()
				# And notify our users that it worked


		except IntegrityError:
			messages.error(
            	self.request, 'Ocorreu um erro ao salvar a Atividade.')

		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, activity_time_form, activity_time_formset):
		return self.render_to_response(
			self.get_context_data(
            	form=form,
            	activity_time_formset=self.activity_time_formset
            )
        )


	def get_context_data(self, **kwargs):
		context = super(CreateActivity,self).get_context_data(**kwargs)
		context['activity_time_formset']=self.activity_time_formset
		return context

class UpdateActivity(UpdateView):
	model = Activity
	form_class = ActivityForm
	template_name = 'activity/add.html'

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		self.activity_time_formset = ActivityTimeFormSet(instance=self.object)
		self.activity_time_formset.extra = 0
		return self.render_to_response(
			self.get_context_data(
           		form=form,
	            activity_time_formset=self.activity_time_formset
	        )
	    )

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.form_class(self.request.POST, instance=self.object)
		self.activity_time_formset = ActivityTimeFormSet(self.request.POST, instance=self.object)

		if form.is_valid() and self.activity_time_formset.is_valid():
			return self.form_valid(form)
		else:
			for form in self.activity_time_formset:
				print("==========",form.errors)
			return self.form_invalid(form)

	def form_valid(self, form):
		self.object = form.save()
		self.activity_time_formset.save()
		return HttpResponseRedirect(reverse('editions:list_activity'))

def activity_delete(request, pk):
	activity= get_object_or_404(Activity, pk=pk)
	activity.delete()
	return JsonResponse({'msg': "Atividade excluida com sucesso!", 'code': "1"})

class DetailActivity(DetailView):
	model = Activity
	template_name = 'activity/detail.html'

	def get_context_data(self, **kwargs):
		self.activity = self.get_object()
		context = super().get_context_data(**kwargs)
		context['times'] = ActivityTime.objects.filter(activity=self.activity.id)
		context['count_inscriptions'] = InscriptionActivity.objects.filter(activity=self.activity.id).count()
		return context


class ListActivity(ListView):

	model = Activity
	http_method_names = ['get']
	template_name = 'activity/list.html'
	context_object_name = 'activity'
	paginate_by = 25

	def get_queryset(self): 
		self.queryset = super(ListActivity, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter( title__icontains = self.request.GET['search_box']) 
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(ListActivity, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
		    startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
		    endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]
		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
		    })
		return context



# InscriptionActivity
class CreateInscriptionActivity(CreateView):
	model = InscriptionActivity
	form_class = InscriptionActivityForm
	template_name = 'inscriptionactivity/add.html'



	def get(self, request, *args, **kwargs):

		return super().get(request , *args , **kwargs)

	def post(self, request, *args, **kwargs):
		self.object = None
		form = self.form_class(self.request.POST)

		if form.is_valid():
			return self.form_valid(form, request)

		else:
			return self.form_invalid(form, request)

	def form_valid(self, form , request):
		

		inscription_activity = form.save(commit=False)

		if InscriptionActivity.objects.filter(participant=inscription_activity.participant).count() == 0:

			inscription_activity.date_of_inscription = datetime.now()
			inscription_activity.inscription = Inscription.objects.filter(user=inscription_activity.participant).first()
			
			inscritos = InscriptionActivity.objects.filter(activity=inscription_activity.activity).count()
			
			if inscritos+1 > inscription_activity.activity.vacancies:
				messages.warning(self.request, 'Não há mais vagas para esta atividade.')
				return HttpResponseRedirect(reverse('editions:add_inscription_activity'))					


			
			if not inscription_activity.inscription:
				messages.warning(self.request, 'Participante não está inscrito na edição atual.')
				return HttpResponseRedirect(reverse('editions:add_inscription_activity'))	
			
			if inscription_activity.inscription.campus != inscription_activity.activity.campus:
				messages.warning(self.request, 'Participante inscrito em outro campus.')
				return HttpResponseRedirect(reverse('editions:add_inscription_activity'))


			else:
				inscription_activity.save()
				return HttpResponseRedirect(reverse('editions:list_inscription_activity'))
		else:

			this_activity_time = ActivityTime.objects.filter(activity=inscription_activity.activity.id)
			all_activitys_time = ActivityTime.objects.all().exclude(activity=inscription_activity.activity.id)

			if InscriptionActivity.objects.filter(participant=inscription_activity.participant,activity=inscription_activity.activity.id).count() > 0:
				messages.warning(self.request, 'Participante inscrito nesta atividade')
				print("Participant ja  inscrito nesta atividade")
				return HttpResponseRedirect(self.get_error_url())
			
			for activity in this_activity_time:
				for others in all_activitys_time:
					if activity.date == others.date:
						if activity.date_start >= others.date_start and activity.date_end <= others.date_end:
							messages.warning(self.request, 'Conflito de Horários com outras atividades')
							return HttpResponseRedirect(reverse('editions:add_inscription_activity'))
					
						
			inscription_activity.date_of_inscription = datetime.now()
			inscription_activity.inscription = Inscription.objects.filter(user=inscription_activity.participant).first()
			inscritos = InscriptionActivity.objects.filter(activity=inscription_activity.activity).count()

			if inscritos+1 > inscription_activity.activity.vacancies:
				messages.warning(self.request, 'Não há mais vagas para esta atividade.')
				return HttpResponseRedirect(reverse('editions:add_inscription_activity'))					

			
			if not inscription_activity.inscription:
				messages.warning(self.request, 'Participante não está inscrito na edição atual.')
				return HttpResponseRedirect(reverse('editions:add_inscription_activity'))	
			
			if inscription_activity.inscription.campus != inscription_activity.activity.campus:
				messages.warning(self.request, 'Participante inscrito em outro campus.')
				return HttpResponseRedirect(reverse('editions:add_inscription_activity'))
			else:
				inscription_activity.save()
				return HttpResponseRedirect(reverse('editions:list_inscription_activity'))						
				

	def get_error_url(self):
		return reverse('editions:add_inscription_activity')

class UpdateInscriptionActivity(UpdateView):
	model = InscriptionActivity
	form_class = InscriptionActivityForm
	template_name = 'inscriptionactivity/add.html'


def inscription_activity_delete(request, pk):
	inscription_activity= get_object_or_404(InscriptionActivity, pk=pk)
	inscription_activity.delete()
	return JsonResponse({'msg': "Inscrição em atividade excluida com sucesso!", 'code': "1"})

class ListInscriptionActivity(ListView):

	model = InscriptionActivity
	http_method_names = ['get']
	template_name = 'inscriptionactivity/list.html'
	context_object_name = 'activity'
	paginate_by = 25

	def get_queryset(self):
		self.queryset = super(ListInscriptionActivity, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter( activity__title__icontains = self.request.GET['search_box']) 
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(ListInscriptionActivity, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
		    startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
		    endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]
		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
		    })
		return context


# ActivityTime
class CreateActivityTime(CreateView):
	model = ActivityTime
	form_class = ActivityTimeForm
	template_name = 'activitytime/add.html'

class UpdateActivityTime(UpdateView):
	model = ActivityTime
	form_class = ActivityTimeForm
	template_name = 'activitytime/add.html'

def activity_time_delete(request , pk):
	activity_time= get_object_or_404(ActivityTime, pk=pk)
	activity_time.delete()
	return JsonResponse({'msg': "Horário de atividade excluida com sucesso!", 'code': "1"})

class ListActivityTime(ListView):

	model = ActivityTime
	http_method_names = ['get']
	template_name = 'activitytime/list.html'
	context_object_name = 'activity'
	paginate_by = 25

	def get_queryset(self):
		self.queryset = super(ListActivityTime, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter( activity__icontains = self.request.GET['search_box']) 
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(ListActivityTime, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
		    startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
		    endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
				if n > 0 and n <= num_pages]
		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
		    })
		return context


# PresenceActivity

class CreatePresenceActivity(DetailView):
	model = Activity
	form_class = InscriptionActivity
	template_name = 'activity/presence.html'


	def get_context_data(self, **kwargs):
		self.activity = self.get_object()
		context = super().get_context_data(**kwargs)
		inscription = InscriptionActivity.objects.filter(activity=self.activity.id)
		context['inscription'] = inscription
		context['activity'] = self.activity
		return context

	def post(self, request, *args, **kwargs):
		self.activity = self.get_object()
		participantes = self.request.POST.getlist('participantes[]') 
		
		for participante in participantes:
			participante_atual = participante.split(',')
			id_participante = participante_atual[0]
			
			status_presenca = participante_atual[1]
			
			inscription = InscriptionActivity.objects.get(pk=id_participante)
			
			if status_presenca == 'true':
				status_presenca = True
				inscription.present = status_presenca
				inscription.save()
			else:
				status_presenca = False
				print("Status ", inscription.present)
				inscription.present = status_presenca
				inscription.save()
				print("Status ", inscription.present)



		return JsonResponse({'msg': "Presenças salvas com sucesso!", 'code': "1"})

# Participant

# Inscription
class CreateInscriptionParticipant(CreateView):
	model = Inscription
	form_class = InscriptionParticipantForm
	template_name = 'inscription/add.html'

	def post(self, request, *args, **kwargs):
		self.object = None
		
		form = self.form_class(self.request.POST)

		if form.is_valid():
			return self.form_valid(form, request)

		else:
			return self.form_invalid(form, request)

	def form_valid(self, form , request):
		inscription = form.save(commit=False)  

		inscription.user = request.user
		inscription.date_of_inscription = datetime.now()
		inscription.edition = Edition.objects.filter(date_start__lte=datetime.now() , date_end__gte=datetime.now(),campus=inscription.campus).first()
		
		if not inscription.edition:
			messages.warning(self.request, 'Periodo de inscrição expirado.')
			return HttpResponseRedirect(reverse('editions:create_incription_participant'))
		else:
			inscription.save()
			messages.success(self.request, 'Inscrição realizada com sucesso.')
		
			return HttpResponseRedirect(reverse('editions:incritption_activity_participant'))


class UpdateInscriptionParticipant(UpdateView):
	model = Inscription
	form_class = InscriptionParticipantForm
	template_name = 'inscription/add.html'
	
	def form_valid(self, form):
		inscription = form.save(commit=False)  

		inscription.user = self.request.user
		inscription.date_of_inscription = datetime.now()
		inscription.edition = Edition.objects.filter(date_start__lte=datetime.now() , date_end__gte=datetime.now()).first()
		
		if not inscription.edition:
			messages.warning(self.request, 'Essa edição já está finalizada.')
			return HttpResponseRedirect(reverse('editions:create_incription_participant'))
		else:
			inscription.save()
			messages.success(self.request, 'Inscrição realizada com sucesso.')
		
			return HttpResponseRedirect(reverse('editions:incritption_activity_participant'))



class ListInscriptionParticipant(ListView):

	model = InscriptionActivity
	http_method_names = ['get']
	template_name = 'inscriptionactivity/list_participant.html'
	context_object_name = 'activity'
	paginate_by = 25

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		inscriptions = InscriptionActivity.objects.filter(participant=self.request.user)
		print(inscriptions)
		context['inscriptions'] = inscriptions
		
		return context


class ListInscriptionEditionParticipant(ListView):

	model = Inscription
	http_method_names = ['get']
	template_name = 'inscription/participant_list.html'
	context_object_name = 'object_list'
	paginate_by = 25

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		inscriptions = Inscription.objects.filter(user=self.request.user)
		edicao = Edition.objects.filter(start_of_registrations__lte=datetime.now() , end_of_registrations__gte=datetime.now()).first()		

		try:
			print("AQTD  ", Inscription.objects.filter(user=self.request.user).count())
		except:
			pass

		context['inscriptions'] = inscriptions
		context['edicao'] = edicao
		
		return context

class DetailActivityParticipant(DetailView):
	model = Activity
	template_name = 'inscriptionactivity/detail.html'

	def get_context_data(self, **kwargs):
		self.activity = self.get_object()
		context = super().get_context_data(**kwargs)
		context['times'] = ActivityTime.objects.filter(activity=self.activity.id)
		return context


class CreateInscriptionParticipantActivity(CreateView):
	model = InscriptionActivity
	form_class = InscriptionActivityParticipantForm
	template_name = 'inscriptionactivity/participant_add.html'


	def get(self, request, *args, **kwargs):

		return super().get(request , *args , **kwargs)

	def post(self, request, *args, **kwargs):
		self.object = None
		form = self.form_class(self.request.POST)

		if form.is_valid():
			return self.form_valid(form, request)

		else:
			return self.form_invalid(form, request)

	def form_valid(self, form , request):
		

		inscription_activity = form.save(commit=False)

		edition = Edition.objects.get(ativo=True)
		data_atual = date.today()
		inscritosAtividade = InscriptionActivity.objects.filter(activity=inscription_activity.activity).count()

		# Verificação da data
		if data_atual < edition.start_of_registrations or data_atual > edition.end_of_registrations:

			messages.warning(self.request, 'Prazo de inscrição inválido.')
			return HttpResponseRedirect(reverse('editions:incritption_activity_participant'))

		#Verifica a quantidade de vagas
		if inscritosAtividade+1 > inscription_activity.activity.vacancies:
			messages.warning(self.request, 'Não há mais vagas para esta atividade.')
			return HttpResponseRedirect(reverse('editions:incritption_activity_participant'))


		# Nao há inscrições deste usuário
		if InscriptionActivity.objects.filter(participant=self.request.user).count() == 0:

			inscription_activity.participant = request.user
			inscription_activity.date_of_inscription = datetime.now()
			inscription_activity.inscription = Inscription.objects.filter(user=self.request.user).first()
				
			inscription_activity.save()
			messages.success(self.request, 'Primeira inscrição realizada com sucesso.')
			return HttpResponseRedirect(reverse('editions:incritption_activity_participant'))

		# Há inscrições
		else:

			# Mesma Atividade
			if InscriptionActivity.objects.filter(activity=inscription_activity.activity,participant=self.request.user):
				messages.warning(self.request, 'Você já está inscrito nesta atividade.')
				return HttpResponseRedirect(reverse('editions:incritption_activity_participant'))
			else:

				# Tabela dessa atividade
				tabela_horarios_atual = ActivityTime.objects.filter(activity=inscription_activity.activity)
				
				# Todas as inscrições do usuário
				todas_as_atividades_inscrito = InscriptionActivity.objects.filter(participant=self.request.user)
				
				# Verifica se ha conflitos
				for horarios in tabela_horarios_atual:
					for atividade in todas_as_atividades_inscrito:
						for tabela_cadastrada in ActivityTime.objects.filter(activity=atividade.activity):
							if horarios.date == tabela_cadastrada.date:

								print(horarios.date_start,horarios.date_end)
								print(tabela_cadastrada.date_start,tabela_cadastrada.date_end)
								
								if (horarios.date_start > tabela_cadastrada.date_start and horarios.date_start < tabela_cadastrada.date_end) or ((horarios.date_end > tabela_cadastrada.date_start and horarios.date_start < tabela_cadastrada.date_end)) :
									messages.error(self.request, 'Conflito de horarios')
									return HttpResponseRedirect(self.get_error_url())							


			inscription_activity.participant = request.user
			inscription_activity.date_of_inscription = datetime.now()
			inscription_activity.inscription = Inscription.objects.filter(user=self.request.user).first()
				
			inscription_activity.save()

			messages.success(self.request, 'Inscrição realizado com sucesso')
			return HttpResponseRedirect(reverse('editions:incritption_activity_participant'))


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
			
		if not Inscription.objects.filter(user=self.request.user).first():
			notInscriptEdition = True
		else:
			notInscriptEdition = False

		inscriptions = InscriptionActivity.objects.filter(participant=self.request.user)
		context['inscriptions'] = inscriptions
		context['notInscriptEdition'] = notInscriptEdition
		return context
				

	def get_error_url(self):
		return reverse('editions:incritption_activity_participant')



# Autocompletes
class UserAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):

		qs = User.objects.all()

		if self.q:
			qs = qs.filter(Q(name__icontains=self.q))

		return qs

class CampusAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):

		qs = Campus.objects.all()

		if self.q:
			qs = qs.filter(Q(name__icontains=self.q))

		return qs

class EditionAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):

		qs = Edition.objects.filter(date_start__lte=datetime.now() , date_end__gte=datetime.now())

		if self.q:
			qs = qs.filter(edition__ativo=True) 

		return qs 

class EditionInscriptionAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):

		qs = Edition.objects.filter(start_of_registrations__lte=date.today() , end_of_registrations__gte=date.today())

		if self.q:
			qs = qs.filter(edition__ativo=True) 

		return qs

class TypeActivityAutocomplete(autocomplete.Select2QuerySetView):

	def get_queryset(self):

		qs = TypeActivity.objects.all()

		if self.q:
			qs = qs.filter(Q(name__icontains=self.q))

		return qs

class InscriptionActivityAutocomplete(autocomplete.Select2QuerySetView):

	def get_queryset(self):
		userLogado = self.request.user
		inscription = Inscription.objects.filter(user=userLogado).first()

		print(inscription.campus)
		qs = Activity.objects.filter(campus=inscription.campus)

		if self.q:
			qs = qs.filter(Q(title__icontains=self.q))

		return qs


class ActivityAllAutocomplete(autocomplete.Select2QuerySetView):

	def get_queryset(self):

		qs = Activity.objects.filter(edition__ativo=True)

		if self.q:
			qs = qs.filter(Q(title__icontains=self.q))

		return qs

# Ceritificate List
class Certificate(View):
	"""
	Classe para lista dos certificados disponíveis do usuário
	"""
	template_name = "certificate/list.html"

	def get(self, request, *args, **kwargs):
		qs = InscriptionActivity.objects.filter(present=True, participant=self.request.user)
		return render(request, self.template_name, {'certificates': qs})
		

# Função para enviar notificação
def send_notification(users):
	from django.core.mail import EmailMultiAlternatives
	from django.template.loader import render_to_string
	from django.utils.html import strip_tags
	from django.conf import settings
	import time

	for user in users:
		html_content = render_to_string('certificate/email.html', {'user': user})
		text_content = strip_tags(html_content)

		subject = "[SEMEX] Um novo certificado disponível para download!"
		from_email = "SEMEX <"+ str(settings.EMAIL_HOST_USER)+">"
		to = [user.email]

		msg = EmailMultiAlternatives(subject, text_content, from_email, to)
		msg.attach_alternative(html_content, "text/html")
		msg.send()
		time.sleep(1)

# Enviar notificação dos certificados
class NotificationCertificates(View):
	"""
	Classe para enviar notificação por email dos certificados
	"""
	template_name = "certificate/notification.html"

	def get(self, request, *args, **kwargs):
		import threading
		import time

		try:
			now_edition = Edition.objects.get(ativo=True, start_of_registrations__lte=datetime.now(), end_of_registrations__gte=datetime.now())
			inscriptions = InscriptionActivity.objects.filter(present=True, activity__edition=now_edition)

			users = [x.participant for x in inscriptions]

			args = {
				'users': users,
			}
			
			t = threading.Thread(target=send_notification, kwargs=args)
			t.start()
			return render(request, self.template_name)

		except:
			pass

		return render(request, self.template_name, {'message': 'Não foi possível enviar as notificações. Não existe uma edição válida na plataforma'})
