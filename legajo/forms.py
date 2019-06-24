from django import forms
from .models import *

class DocenteForm(forms.ModelForm):
	class Meta: 
		model = DOCENTE
		fields = '__all__'

		widgets ={
		"DOC_COD" : forms.TextInput(attrs={'class': 'form-control'}),	
		"DOC_DNI" : forms.TextInput(attrs={'class': 'form-control'}),	
		"DOC_CELU" :  forms.TextInput(attrs={'class': 'form-control'}),  
		"DOC_EMAIL" :  forms.TextInput(attrs={'class': 'form-control'}), #cambiar por EmailField()
		"DOC_NOMBRE" : forms.TextInput(attrs={'class': 'form-control'}),
		"DOC_APE" :  forms.TextInput(attrs={'class': 'form-control'}),
		"DOC_SEXO" :  forms.TextInput(attrs={'class': 'form-control'}),
		"DOC_NAC" :  forms.DateInput(attrs={'class': 'form-control'}),
		"DOC_ESTADO" :  forms.TextInput(attrs={'class': 'form-control'})
		}


			