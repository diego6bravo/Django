from django.urls import path, re_path
from .import views
from .views import Figma
from .views import ListaEmpleados
from .views import CrearEmpleados
from .views import DetalleEmpleados
from .views import ActualizarEmpleados
from .views import BorrarEmpleados

urlpatterns = [    
    path('', views.index, name='index'),
    path('otrapagina/', views.otrapagina, name='otrapagina'),
    path('lemon/', views.lemon, name='lemon'),
    path('little/', views.little, name='little'),
    path('litlogueo/', views.litlogueo, name='litlogueo'),
    path('tabmenu/', views.tabmenu, name='tabmenu'),
    path('menubd/', views.menubd, name='menubd'),
    path('vistafor/', views.vistafor, name='vistafor'),
    path('cobros/', views.cobros, name='cobros'),
    path('home/', views.home, name='home'),
    path('getuser/<name>/<id>', views.pathview, name='pathview'), 
    path('getuser/', views.qryview, name='qryview'), 
    path("showform/", views.showform, name="showform"), 
    path("getform/", views.getform, name='getform'),
    path("platos/<str:plato>", views.menu, name='menu'),
    path("drinks/<str:drinks_name>", views.drinks, name='drinks'),
    path("myview/", views.myview, name='myview'),
    path("my_error/", views.my_error, name='my_error'),
    path("change/", views.change, name='change'),
    path("content/", views.content, name='content'),
    path("formul/", views.formul, name='formul'),
    path("figmadet/", views.home_figma, name='home_figma'),
    path("listafigma/", views.list_detalle, name='list'),
    path('lista_detalle_emp/<int:id>/', views.mostrar_list_detalle, name="list_detalle"),

    #Vistas Genéricas}
    path('figma_view/', Figma.as_view(), name='figma_view'),
    path('figma_list/', ListaEmpleados.as_view(), name='figma_list'), 
    path('figma_create/', CrearEmpleados.as_view(), name = 'CrearEmp'),
    path('figma_detail/<int:pk>', DetalleEmpleados.as_view(), name='figma_detail'), 
    path('figma_update/<int:pk>', ActualizarEmpleados.as_view(), name='figma_update'),
    path('figma_delete/<int:pk>', BorrarEmpleados.as_view(), name='figma_delete'), 
] 

