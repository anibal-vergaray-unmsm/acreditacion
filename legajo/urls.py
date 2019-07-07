from django.urls import path, include
from . import views


urlpatterns = [
    path('index',views.index,name='index'),
    path('list_profesor',views.list_profesor,name='list_profesor'),
    path('list_curso',views.list_curso,name='list_curso'),
    path('list_expdocente',views.list_expdocente,name='list_expdocente'),
    path('list_institucion',views.list_institucion,name='list_institucion'),
    path('list_explaboral',views.list_explaboral,name='list_explaboral'),
    path('list_entidad',views.list_entidad,name='list_entidad'),
    path('list_group',views.list_group,name='list_group'),
    path('list_titulo',views.list_titulo,name='list_titulo'),
    path('list_espec',views.list_espec,name='list_espec'),
    path('list_produc',views.list_produc,name='list_produc'),
    path('list_resol',views.list_resol,name='list_resol'),
    path('list_eval',views.list_eval,name='list_eval'),
    path('list_cargo',views.list_cargo,name='list_cargo'),
    #CreateView
    path('create_profesores',views.DocenteCreate.as_view(),name='create_profesores'),
    path('add_curso',views.CursoCreate.as_view(),name='add_curso'),
    path('add_institucion',views.InstitucionCreate.as_view(),name='add_institucion'),
    path('add_entidad',views.EntidadCreate.as_view(),name='add_entidad'),
    path('add_explaboral',views.expLaboralCreate.as_view(),name='add_explaboral'),
    path('add_expdocente',views.expDocenteCreate.as_view(),name='add_expdocente'),
    path('add_group',views.GroupCreate.as_view(),name='add_group'),
    path('add_titulo',views.TituloCreate.as_view(),name='add_titulo'),
    path('add_espec', views.EspecCreate.as_view(), name='add_espec'),
    path('add_produc', views.ProducCreate.as_view(), name='add_produc'),
    path('add_resol', views.ResolCreate.as_view(), name='add_resol'),
    path('add_eval', views.EvalCreate.as_view(), name='add_eval'),
    path('add_cargo', views.CargoCreate.as_view(), name='add_cargo'),

    #UpdateView
    path(r'edit_profesor/(?P<pk>\d+)/$/',views.DocenteEdit.as_view(),name='edit_profesor') ,
    #DeleteView
    path(r'delete_profesor/(?P<pk>\d+)/$/',views.DocenteDelete.as_view(),name='delete_profesor'),
]