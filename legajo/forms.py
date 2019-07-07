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


class CursoForm(forms.ModelForm):
	class Meta:
		model = CURSO
		fields = '__all__'

		widgets = {
			"CUR_COD" : forms.TextInput(attrs={'class':'form-control'}),
			"CUR_CRED": forms.NumberInput(attrs={'class': 'form-control'}),
			"CUR_HOR_SEM": forms.NumberInput(attrs={'class':'form-control'}),
			"CUR_CICLO": forms.TextInput(attrs={'class': 'form-control'}),
			"CUR_SEMES": forms.TextInput(attrs={'class': 'form-control'}),
			"CUR_NOMBRE": forms.TextInput(attrs={'class': 'form-control'}),
			"docentes": forms.SelectMultiple(attrs={'class': 'form-control'}),
		}

class InstitucionForm(forms.ModelForm):
	class Meta:
		model = INSTITUCION
		fields = '__all__'

		widgets = {
			"INSTI_NOMBRE" : forms.TextInput(attrs={'class':'form-control'}),
			"INSTI_PAIS": forms.TextInput(attrs={'class':'form-control'}),
			"INSTI_TIPO": forms.TextInput(attrs={'class':'form-control'}),
		}

class EntidadForm(forms.ModelForm):
	class Meta:
		model = ENTIDAD
		fields = '__all__'

		widgets = {
			"ENT_NOMBRE" : forms.TextInput(attrs={'class':'form-control'}),
			"ENT_SECTOR": forms.TextInput(attrs={'class': 'form-control'}),
			"ENT_RUBRO": forms.TextInput(attrs={'class': 'form-control'}),
		}

class expLaboralForm(forms.ModelForm):
	class Meta:
		model = experienciaLABORAL
		fields = '__all__'

		widgets = {
			"EXL_CARGO" : forms.TextInput(attrs={'class':'form-control'}),
			"EXL_FECHA_INI": forms.DateInput(attrs={'class':'form-control'}),
			"EXL_FECHA_FIN": forms.DateInput(attrs={'class':'form-control'}),
			"EXL_SUELDO": forms.NumberInput(attrs={'class':'form-control'}),
			"EXL_DESCRIP": forms.TextInput(attrs={'class':'form-control'}),
			"entidad": forms.Select(attrs={'class':'form-control'}),
			"docentes": forms.Select(attrs={'class':'form-control'}),
		}


class expDocenteForm(forms.ModelForm):
	class Meta:
		model = experienciaDOCENTE
		fields = '__all__'

		widgets = {
			"EXD_FECHA_INI" : forms.DateInput(attrs={'class':'form-control'}),
			"EXD_FECHA_FIN": forms.DateInput(attrs={'class':'form-control'}),
			"EXD_CARGO": forms.TextInput(attrs={'class':'form-control'}),
			"docente": forms.Select(attrs={'class':'form-control'}),
			"institucion": forms.Select(attrs={'class': 'form-control'}),
		}

class GroupForm(forms.ModelForm):
	class Meta:
		model = grupoInvestigacion
		fields = '__all__'

		widgets = {
			"GI_TEMA" : forms.TextInput(attrs={'class':'form-control'}),
			"GI_NOMBRE": forms.TextInput(attrs={'class':'form-control'}),
			"GI_INV_PRINCIPAL": forms.TextInput(attrs={'class':'form-control'}),
			"GI_FECHA_INI": forms.DateInput(attrs={'class':'form-control'}),
			"GI_FECHA_FIN": forms.DateInput(attrs={'class': 'form-control'}),
			"GI_DESCRIPCION": forms.TextInput(attrs={'class': 'form-control'}),
			"docentes": forms.SelectMultiple(attrs={'class': 'form-control'}),
		}

class TituloForm(forms.ModelForm):
	class Meta:
		model = TITULO
		fields = '__all__'

		widgets = {
			"TIT_NOMBRE" : forms.TextInput(attrs={'class':'form-control'}),
			"TIT_TIPO": forms.TextInput(attrs={'class': 'form-control'}),
			"TIT_INI": forms.DateInput(attrs={'class':'form-control'}),
			"TIT_FIN": forms.DateInput(attrs={'class': 'form-control'}),
			"docente": forms.Select(attrs={'class': 'form-control'}),
			"institucion": forms.Select(attrs={'class': 'form-control'}),
		}

class EspecForm(forms.ModelForm):
	class Meta:
		model = ESPECIALIZACION
		fields = '__all__'

		widgets = {
			"ESP_TIPO" : forms.TextInput(attrs={'class':'form-control'}),
			"ESP_NOMBRE": forms.TextInput(attrs={'class': 'form-control'}),
			"ESP_FECHA_INI": forms.DateInput(attrs={'class':'form-control'}),
			"ESP_FECHA_FIN": forms.DateInput(attrs={'class': 'form-control'}),
			"docente": forms.Select(attrs={'class': 'form-control'}),
			"institucion": forms.Select(attrs={'class': 'form-control'}),
		}

class ProducForm(forms.ModelForm):
	class Meta:
		model = produccionCIENTFICA
		fields = '__all__'

		widgets = {
			"PROD_TIPO" : forms.TextInput(attrs={'class':'form-control'}),
			"PROD_TITULO": forms.TextInput(attrs={'class': 'form-control'}),
			"PROD_PRIMER_AUTOR": forms.TextInput(attrs={'class':'form-control'}),
			"PROD_FECHA": forms.DateInput(attrs={'class': 'form-control'}),
			"PROD_REPOSI": forms.TextInput(attrs={'class': 'form-control'}),
			"PROD_URL": forms.URLInput(attrs={'class': 'form-control'}),
			"docentes": forms.SelectMultiple(attrs={'class': 'form-control'}),
		}

class ResolForm(forms.ModelForm):
	class Meta:
		model = RESOLUCION
		fields = '__all__'

		widgets = {
			"RES_FECHA" : forms.DateInput(attrs={'class':'form-control'}),
			"RES_DESCRIP": forms.TextInput(attrs={'class': 'form-control'}),
			"RES_EXPEDIENTE": forms.TextInput(attrs={'class':'form-control'}),
			"RES_TIPO": forms.TextInput(attrs={'class': 'form-control'}),
			"RES_CATEG": forms.TextInput(attrs={'class': 'form-control'}),
			"RES_CLASE": forms.TextInput(attrs={'class': 'form-control'}),
		}

class EvalForm(forms.ModelForm):
	class Meta:
		model = evaluacionyPerfeccionamiento
		fields = '__all__'

		widgets = {
			"EVA_TIPO" : forms.TextInput(attrs={'class':'form-control'}),
			"EVA_OBSERVACION": forms.TextInput(attrs={'class': 'form-control'}),
			"docentes": forms.Select(attrs={'class': 'form-control'}),
			"resolucion": forms.Select(attrs={'class': 'form-control'}),
		}

class CargoForm(forms.ModelForm):
	class Meta:
		model = CARGO
		fields = '__all__'

		widgets = {
			"CAR_NOM" : forms.TextInput(attrs={'class':'form-control'}),
			"CAR_DESCRIP": forms.TextInput(attrs={'class': 'form-control'}),
			"docente": forms.Select(attrs={'class': 'form-control'}),
			"resolucion": forms.Select(attrs={'class': 'form-control'}),
		}