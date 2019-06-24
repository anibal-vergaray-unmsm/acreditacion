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
    path('create_profesores',views.DocenteCreate.as_view(),name='create_profesores') ,
    path(r'edit_profesor/(?P<pk>\d+)/$',views.DocenteEdit.as_view(),name='edit_profesor') ,
    path(r'delete_profesor/(?P<pk>\d+)/$',views.DocenteDelete.as_view(),name='delete_profesor') ,
]
