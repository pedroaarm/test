from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from dal import autocomplete
from django.contrib.auth import get_user_model
from dal import autocomplete
from accounts.models import User

from .models import *

 
class CampusForm(forms.ModelForm): 

    class Meta:
        model = Campus
        fields = ['name']


class TypeActivityForm(forms.ModelForm): 

    class Meta:
        model = TypeActivity
        fields = ['name']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name']

class EditionForm(forms.ModelForm):

	class Meta:
		model = Edition
		fields = ['date_start' , 'date_end' , 'edition','campus','start_of_registrations','end_of_registrations','organizers','qtd_max_authors','start_submissions','end_submissions']

		widgets = {
            'campus': autocomplete.ModelSelect2Multiple(url='editions:campus_autocomplete'),
            'organizers': autocomplete.ModelSelect2Multiple(url='editions:user_autocomplete'),

        }	

# For admin
class InscriptionForm(forms.ModelForm):
    
	user = forms.ModelChoiceField(
		required=True,
		queryset = User.objects.all(),
		label = "Participante",
		widget = autocomplete.ModelSelect2(url='editions:user_autocomplete',attrs={'data-width': '100%'})
	)


	campus = forms.ModelChoiceField(
		required=True,
		queryset = Campus.objects.all(),
		label = "Campus",
		widget = autocomplete.ModelSelect2(url='editions:campus_autocomplete')
	)

	class Meta:
		model = Inscription
		fields = ['user','campus']


# For participant
class InscriptionParticipantForm(forms.ModelForm):
    
	campus = forms.ModelChoiceField(
		required=True,
		queryset = Campus.objects.all(),
		label = "Campus",
		widget = autocomplete.ModelSelect2(url='editions:campus_autocomplete')
	)

	class Meta:
		model = Inscription
		fields = ['campus']

class ActivityForm(forms.ModelForm):


	edition = forms.ModelChoiceField(
		required=True,
		queryset = Edition.objects.all(),
		label = "Edição",
		widget = autocomplete.ModelSelect2(url='editions:edition_autocomplete')
	)

	type_of_activity = forms.ModelChoiceField(
		required=True,
		queryset = TypeActivity.objects.all(),
		label = "Tipo de Atividade",
		widget = autocomplete.ModelSelect2(url='editions:type_activity_autocomplete')
	)

	campus = forms.ModelChoiceField(
		required=True,
		queryset = Campus.objects.all(),
		label = "Campus",
		widget = autocomplete.ModelSelect2(url='editions:campus_autocomplete')
	)

	class Meta:
		model = Activity
		fields = ['title' , 'type_of_activity' , 'professional' ,'location' ,'vacancies','workload','description','edition' ,'campus']

ActivityTimeFormSet = forms.inlineformset_factory(
	Activity, ActivityTime, fields=('date', 'date_start', 'date_end'), extra=1)

class InscriptionActivityForm(forms.ModelForm):
 
	participant = forms.ModelChoiceField(
		required=True,
		queryset = User.objects.all(),
		label = "Participante",
		widget = autocomplete.ModelSelect2(url='editions:user_autocomplete')
	)


	activity  = forms.ModelChoiceField(
		required=True,
		queryset = Activity.objects.all(),
		label = "Atividade",
		widget = autocomplete.ModelSelect2(url='editions:all_activity_autocomplete')
	)

	class Meta:
		model = InscriptionActivity 
		fields = ['participant','activity']

# For Participant
class InscriptionActivityParticipantForm(forms.ModelForm):
   
    activity  = forms.ModelChoiceField(
		required=True,
		queryset = Activity.objects.all(),
		label = "Atividade",
		widget = autocomplete.ModelSelect2(url='editions:inscription_activity_autocomplete')
	)

    class Meta:
        model = InscriptionActivity 
        fields = ['activity']


class ActivityTimeForm(forms.ModelForm):
	activity  = forms.ModelChoiceField(
		required=True,
		queryset = Activity.objects.all(),
		label = "Atividade",
		widget = autocomplete.ModelSelect2(url='editions:inscription_activity_autocomplete')
	)

	class Meta:
		model = ActivityTime
		fields = ['date_start' ,'date_end','activity' ,'date']