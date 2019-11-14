from django.urls import path
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import views as auth_views
from .views import *
from .forms import *
from django.urls import reverse_lazy

app_name = 'editions'
 
urlpatterns = [
	# Campus
 	path('campus-add/', CreateCampus.as_view(), name='add_campus',),
 	path('campus-list/', ListCampus.as_view(), name='list_campus',),
 	path('campus-edit/<int:pk>/', UpdateCampus.as_view(), name='edit_campus',),
 	path('campus-delete/<int:pk>/', campus_delete, name='delete_campus',),

 	# typeActivity
 	path('tipo-atividade-add/',CreateTypeActivity.as_view(), name='add_type_activity',),
 	path('tipo-atividade-list/',ListTypeActivity.as_view(), name='list_type_activity',),
 	path('tipo-atividade-edit/<int:pk>/', UpdateTypeActivity.as_view(), name='edit_typeactivity',),
 	path('tipo-atividade-delete/<int:pk>/', typeactivity_delete, name='delete_typeactivity',),


 	# Location
 	path('lugar-add/',CreateLocation.as_view(), name='add_location',),
 	path('lugar-list/',ListLocation.as_view(), name='list_location',),
 	path('lugar-edit/<int:pk>/', UpdateLocation.as_view(), name='edit_location',),
 	path('lugar-delete/<int:pk>/', location_delete, name='delete_location',),

 	# Editions
 	path('edicao-add/',CreateEdition.as_view(), name='add_edition',),
 	path('edicao-list/',ListEdition.as_view(), name='list_edition',),
	path('edicao-edit/<int:pk>/', UpdateEdition.as_view(), name='edit_edition',),
	path('edicao-detail/<int:pk>/', DetailEdition.as_view(), name='detail_edition',),
	path('edicao-delete/<int:pk>/', edition_delete, name='delete_edicao',),
 	
 	# Incription
 	path('inscricao-add/',CreateInscription.as_view(), name='add_inscription',),
 	path('inscricao-list/',ListInscription.as_view(), name='list_inscription',),
 	path('inscricao-delete/<int:pk>/', inscription_delete, name='delete_inscription',),
	path('inscricao-edit/<int:pk>/', UpdateInscription.as_view(), name='edit_inscription',),


	# Activity 
 	path('atividade-add/',CreateActivity.as_view(), name='add_activity',),
 	path('atividade-list/',ListActivity.as_view(), name='list_activity',),
	path('atividade-edit/<int:pk>/', UpdateActivity.as_view(), name='edit_activity',),
 	path('atividade-delete/<int:pk>/', activity_delete, name='delete_activity',), 
 	path('atividade-detail/<int:pk>/', DetailActivity.as_view(), name='detail_activity',),
 
 	#InscriptionActivity
 	path('inscricao-atividade-add/',CreateInscriptionActivity.as_view(), name='add_inscription_activity',),
 	path('inscricao-atividade-list/',ListInscriptionActivity.as_view(), name='list_inscription_activity',),
	path('inscricao-atividade-edit/<int:pk>/', UpdateInscriptionActivity.as_view(), name='edit_inscription_activity',),
 	path('inscricao-atividade-delete/<int:pk>/', inscription_activity_delete, name='delete_inscription_activity',), 

 	# ActivityTime
 	path('tempo-atividade-add/',CreateActivityTime.as_view(), name='add_activity_time',),
 	path('tempo-atividade-list/',ListActivityTime.as_view(), name='list_activity_time',),
 	path('tempo-atividade-edit/<int:pk>/',UpdateActivityTime.as_view(), name='edit_activity_time',),
 	path('tempo-atividade-delete/<int:pk>/', activity_time_delete, name='delete_activity_time',),  

	# PresenceActivity
	path('presenca-atividade-add/<int:pk>/', CreatePresenceActivity.as_view(), name='presence_activity',),
 	
 	#autocompletes
 	path('user-autocomplete/',UserAutocomplete.as_view(), name='user_autocomplete',),
 	path('campus-autocomplete/',CampusAutocomplete.as_view(), name='campus_autocomplete',),
 	path('edition-autocomplete/',EditionAutocomplete.as_view(), name='edition_autocomplete',),
 	path('edition-inscricao-autocomplete/',EditionInscriptionAutocomplete.as_view(), name='edition_inscription_autocomplete',),
 	path('tipo-atividade-autocomplete/',TypeActivityAutocomplete.as_view(), name='type_activity_autocomplete',),
 	path('inscricao-atividade-autocomplete/',InscriptionActivityAutocomplete.as_view(), name='inscription_activity_autocomplete',), 
 	path('todas-atividades-autocomplete/',ActivityAllAutocomplete.as_view(), name='all_activity_autocomplete',), 

 	# Participants
 	path('inscricao-participant-add/',CreateInscriptionParticipant.as_view(), name='create_incription_participant',),
 	path('inscricao-participant-list/',ListInscriptionParticipant.as_view(), name='list_incription_participant',),
 	path('edicao-participant-list/',ListInscriptionEditionParticipant.as_view(), name='edicao_incription_participant',),
 	path('atividade-detail-participant/<int:pk>/', DetailActivityParticipant.as_view(), name='detail_activity_participant',),
 	path('inscricao-participante-atividade/', CreateInscriptionParticipantActivity.as_view(), name='incritption_activity_participant',),
	path('inscricao-participante-edit/<int:pk>/', UpdateInscriptionParticipant.as_view(), name='edit_inscription_participant',),

	# Certificate
	path('certificates/', Certificate.as_view(), name='certificates'),
	path('notification-certificates/', NotificationCertificates.as_view(), name='notification-certificate'),

] 