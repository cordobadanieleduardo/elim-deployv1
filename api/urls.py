from django.urls import path
from .views import ClienteList, GastoConductorList, GastoConductorAPIList, gastoConductorListReload, gastoConductorList

urlpatterns = [
    path('v1/clientes',ClienteList.as_view(),name='cliente_list'),
    # path('v1/gastos',GastoConductorAPIList.as_view(),name='gastos_list'),
    # path('v1/gastos/reload/view',GastoConductorList.as_view(),name='gastos_list_reload_view'),
    # path('v1/gastos/reload/',gastoConductorList,name='gastos_list_reload'),
    path('v1/gastos/reload/',gastoConductorListReload,name='gastos_list_reload'),
    # path('v1/gastos/reload/(?:fecha=(?P<str:fecha>)/)?$',gastoConductorListReload,name='gastos_list_reload_f'),
    # path('v1/gastos/reload/(?:page-(?P<page_number>[0-9]+)/)?$',gastoConductorListReload,name='gastos_list_reload'),
]