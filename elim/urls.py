from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

#from .views import *
from . import views
from .reportes import reporte_registros


urlpatterns = [
    path('clientes/',views.ClienteView.as_view(), name='cliente_list'),
    path('clientes/new/',views.ClienteNew.as_view(), name='cliente_new'),
    path('clientes/edit/<int:pk>',views.ClienteEdit.as_view(), name='cliente_edit'),
    path('clientes/inactivar/<int:id>',views.cliente_inactivar, name='cliente_inactivar'),
    path('clientes/delete/<int:pk>',views.ClienteDel.as_view(), name='cliente_del'),

    path('vehiculos/',views.VehiculoView.as_view(), name='vehiculo_list'),
    path('vehiculos/new/',views.VehiculoNew.as_view(), name='vehiculo_new'),
    path('vehiculos/edit/<str:pk>',views.VehiculoEdit.as_view(), name='vehiculo_edit'),
    path('vehiculos/inactivar/<str:pk>',views.vehiculo_inactivar, name='vehiculo_inactivar'),


    path('proveedores/',views.ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new',views.ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>',views.ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedores/delete/<int:pk>',views.ProveedorDel.as_view(), name='proveedor_del'),
    
    path('conductor/',views.ConductorView.as_view(), name='conductor_view'),
    path('conductor/edit/<str:pk>',views.ConductorEdit.as_view(), name='conductor_edit'),
    
    # path('servicios/',ServicioView.as_view(), name='servicio_list'),
    # path('servicios/new',ServicioNew.as_view(), name='servicio_new'),
    # path('servicios/edit/<int:pk>',ServicioEdit.as_view(), name='servicio_edit'),
    # path('servicios/delete/<int:pk>',ServicioDel.as_view(), name='servicio_del'),

    # path('servicios/o',servicio_new, name='servicio_def'),

    # path('servicios/u',MuseoCreateView.as_view(), name='museo-add'),


    path('registros/',views.RegistroView.as_view(), name='reg_list'),
    # path('registros/new',views.RegistroNew.as_view(), name='reg_new'),
    # path('registros/edit/<int:pk>',views.RegistroEdit.as_view(), name='reg_edit'),
    path('registros/new',views.reg_add_edit, name='reg_new'),
    path('registros/edit/<int:id>',views.reg_add_edit, name='reg_edit'),
    # path('registros/inactivar/<int:id>',views.cliente_inactivar, name="cliente_inactivar"),

    path('registros/lista/direccion/',views.TrayectoView.as_view(), name='reg_direccion_new'),
    path('registros/direccion/new/',views.TrayectoNew.as_view(), name='reg_direccion_add_new'),

    path('prueba/', views.index, name="index"),
    path('js', views.index_js, name="index-js"),
    path('localizacion', views.localizacion, name="local"),
    
    
    path('trayectos/', views.HomeTrayectosView.as_view(), name='trayecto_view'), 
    path('trayectos/<int:pk>', views.ActInaTrayectoView.as_view(), name='actina_view'), 
    path('rutas/', views.rutas, name="route"),
    path('geocoding/<int:pk>', views.GeocodingView.as_view(), name='geocoding_view'),     
    path('distance', views.DistanceView.as_view(), name='my_distance_view'), 
    

    path('gastos/',views.GastoConductorView.as_view(), name='gasto_list'),
    # path('gastos/',views.gastoConductorView, name='gasto_list'),
    path('gastos/new/',views.GastoConductorNew.as_view(), name='gasto_new'),
    path('gastos/edit/<int:pk>',views.GastoConductorEdit.as_view(), name='gasto_edit'),
    path('gastos/detail/<int:pk>',views.GastoConductorDetailView.as_view(), name='gasto_detail'),
    
    path('map/', views.MapView.as_view(), name='my_map_view'), 
    path('map/conductor/', views.MapConductorView.as_view(), name='conductor_map_view'), 
    path('route/', views.route, name="route"),

    path('reporte/', reporte_registros, name='registros_print_all'),
    
    path('reporte/list/',views.ReporteView.as_view(), name='repo_list'),    
    path('reporte/detail/<int:pk>',views.ReporteDetailView.as_view(), name='repo_detail'),
    
    path('conductor/viaje/reporte/list/',views.ViajeView.as_view(), name='repo_viaje_list'),    
    path('conductor/viaje/reporte/detail/<int:pk>',views.ViajeDetailView.as_view(), name='repo_viaje_detail'),
    
    path('status/',views.StatusDetailView.as_view(), name='status_list'),
    path('status/<str:pk>/',views.vehiculo_activar_inactivar, name='status_activarinact_list'),
    # path('status/<str:pk>/(?:page(?P<page_number>[0-9]+)/)?$',views.vehiculo_activar_inactivar, name='status_activarinact_list'),
    path('status/mecanico/<str:pk>/',views.vehiculo_cambiar_mecanico, name='status_cambiar_mecanico_list'),
    path('status/restaurante/<str:pk>/',views.vehiculo_cambiar_restaurante, name='status_cambiar_restaurante_list'),
    path('status/enfermo/<str:pk>/',views.vehiculo_cambiar_enfermo, name='status_cambiar_enfermo_list'),
    path('status/color/<str:pk>/',views.vehiculo_status_disponibilidad, name='status_cambiar_color_list'),
    path('status/edit/<str:pk>/',views.StatusEdit.as_view(), name='status_edit'),
    
    path('panel/',views.panelView, name='panel_view'),
]


router = DefaultRouter()
router.register("api/paises", views.PaisesViewSet, basename="paises")
router.register("api/museos", views.MuseoViewSet, basename="museos_list")
router.register("api/clientes", views.ClientesViewSet, basename="clientes")
router.register("v1/clientes/", views.ClientesViewSet, basename="clientes_list")
# router.register("v1/gastos", views.GastoConductorViewSet, basename="gastos__list")

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

