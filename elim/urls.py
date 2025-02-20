from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

#from .views import *
from . import views


urlpatterns = [
    path('clientes/',views.ClienteView.as_view(), name='cliente_list'),
    path('clientes/new/',views.ClienteNew.as_view(), name='cliente_new'),
    path('clientes/edit/<int:pk>',views.ClienteEdit.as_view(), name='cliente_edit'),
    path('clientes/inactivar/<int:id>',views.cliente_inactivar, name='cliente_inactivar'),
    path('clientes/delete/<int:pk>',views.ClienteDel.as_view(), name='cliente_del'),

    path('vehiculos/',views.VehiculoView.as_view(), name='vehiculo_list'),
    path('vehiculos/new/',views.VehiculoNew.as_view(), name='vehiculo_new'),
    path('vehiculos/edit/<int:pk>',views.VehiculoEdit.as_view(), name='vehiculo_edit'),
    path('vehiculos/inactivar/<int:id>',views.vehiculo_inactivar, name='vehiculo_inactivar'),


    path('proveedores/',views.ProveedorView.as_view(), name='proveedor_list'),
    path('proveedores/new',views.ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedores/edit/<int:pk>',views.ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedores/delete/<int:pk>',views.ProveedorDel.as_view(), name='proveedor_del'),
    
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
    
    
    path('map', views.MapView.as_view(), name='my_map_view'), 
    path('route', views.route, name="route"),


#     path('subcategorias/',SubCategoriaView.as_view(), name='subcategoria_list'),
#     path('subcategorias/new',SubCategoriaNew.as_view(), name='subcategoria_new'),
#     path('subcategorias/edit/<int:pk>',SubCategoriaEdit.as_view(), name='subcategoria_edit'),
#     path('subcategorias/delete/<int:pk>',SubCategoriaDel.as_view(), name='subcategoria_del'),

#     path('marcas/',MarcaView.as_view(), name="marca_list"),
#     path('marcas/new',MarcaNew.as_view(), name="marca_new"),
#     path('marcas/edit/<int:pk>',MarcaEdit.as_view(), name="marca_edit"),
#     path('marcas/inactivar/<int:id>',marca_inactivar, name="marca_inactivar"),

#     path('um/',UMView.as_view(), name="um_list"),
#     path('um/new',UMNew.as_view(), name="um_new"),
#     path('um/edit/<int:pk>',UMEdit.as_view(), name="um_edit"),
#     path('um/inactivar/<int:id>',um_inactivar, name="um_inactivar"),

#     path('productos/',ProductoView.as_view(), name="producto_list"),
#     path('productos/new',ProductoNew.as_view(), name="producto_new"),
#     path('productos/edit/<int:pk>',ProductoEdit.as_view(), name="producto_edit"),
#     path('productos/inactivar/<int:id>',producto_inactivar, name="producto_inactivar"),
]


router = DefaultRouter()
router.register("api/paises", views.PaisesViewSet, basename="paises")
router.register("api/museos", views.MuseoViewSet, basename="museos_list")
router.register("api/clientes", views.ClientesViewSet, basename="clientes")
router.register("v1/clientes/", views.ClientesViewSet, basename="clientes_list")

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

