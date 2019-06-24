from django.shortcuts import render
from django.views.generic.edit import *
from django.urls import reverse
from .forms import *
from .models import *

def index(request):
    return render(request,template_name='index.html',)

def list_profesor(request):
    profesor = DOCENTE.objects.all()
    return render(request,template_name='list_profesor.html',context={'profesor':profesor})

def list_curso(request):
    curso = CURSO.objects.all()
    return render(request,template_name='list_curso.html',context={'curso':curso})

def list_expdocente(request):
    expdocente = experienciaDOCENTE.objects.all()
    return render(request,template_name='list_expdocente.html',context={'expdocente':expdocente})

def list_institucion(request):
    institucion = INSTITUCION.objects.all()
    return render(request,template_name='list_institucion.html',context={'institucion':institucion})

def list_explaboral(request):
    explaboral = experienciaLABORAL.objects.all()
    return render(request,template_name='list_explaboral.html',context={'explaboral':explaboral})

def list_entidad(request):
    entidad = ENTIDAD.objects.all()
    return render(request,template_name='list_entidad.html',context={'entidad':entidad})

def list_group(request):
    group = grupoInvestigacion.objects.all()
    return render(request,template_name='list_group.html',context={'group':group})

def list_titulo(request):
    titulo = TITULO.objects.all()
    return render(request,template_name='list_titulo.html',context={'titulo':titulo})

def list_espec(request):
    espec = ESPECIALIZACION.objects.all()
    return render(request,template_name='list_espec.html',context={'espec':espec})

def list_produc(request):
    produc = produccionCIENTFICA.objects.all()
    return render(request,template_name='list_produc.html',context={'produc':produc})

def list_resol(request):
    resol = RESOLUCION.objects.all()
    return render(request,template_name='list_resol.html',context={'resol':resol})

def list_eval(request):
    eval= evaluacionyPerfeccionamiento.objects.all()
    return render(request,template_name='list_eval.html',context={'eval':eval})

def list_cargo(request):
    cargo = CARGO.objects.all()
    return render(request,template_name='list_cargo.html',context={'cargo':cargo})

class DocenteCreate(CreateView):
    model= DOCENTE
    form_class= DocenteForm
    template_name='add_docente.html'

    def get_success_url(self):
        return reverse('list_profesor')

class DocenteEdit(UpdateView):
    model= DOCENTE
    form_class= DocenteForm
    template_name='edit_docente.html'

    def get_success_url(self):
        return reverse('list_profesor')

class DocenteDelete(DeleteView):
    model= DOCENTE
    form_class= DocenteForm
    template_name='delete_profesor.html'
    
    def get_context_data(self,**kwargs):
        context_data = super(DocenteDelete,self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        docente =DOCENTE.objects.get(id=int(pk))
        context_data.update({'docente':docente})
        return context_data
        
    def get_success_url(self):
        return reverse('list_profesor')