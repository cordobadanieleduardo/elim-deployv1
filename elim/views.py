from django.utils import timezone
from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from rest_framework import viewsets, filters
from django_filters.rest_framework import  DjangoFilterBackend
from .serializers import MuseoSerializer, PaisSerializer,ClienteSerializer

from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Cliente,Proveedor,Servicio,Vehiculo,Programador,Trayecto,Persona,Museo, Pais, Registro, Locations,Distances
from .forms import ClienteForm,ProveedorForm,\
                ServicioForm, MuseoForm , RegistroForm,\
                DistanceForm, TrayectoForm, VehiculoForm

from bases.views import SinPrivilegios
from django.views import View
from datetime import datetime
from django.conf import settings


import json
import requests
import googlemaps



# Create your views base.

class VistaBaseCreate(SuccessMessageMixin,SinPrivilegios, \
    generic.CreateView):
    context_object_name = 'obj'
    success_message="Registro agregado satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class VistaBaseEdit(SuccessMessageMixin,SinPrivilegios, \
    generic.UpdateView):
    context_object_name = 'obj'
    success_message="Registro actualizado satisfactoriamente"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form) 


# Bloque views cliente.

class ClienteView(SinPrivilegios, generic.ListView):
    permission_required = "elim.view_cliente"
    model = Cliente
    template_name = "elim/cliente_list.html"
    context_object_name = "obj"
    ordering = ['nombre']

class ClienteNew(VistaBaseCreate):
    model = Cliente
    template_name="elim/cliente_form.html"
    context_object_name = "obj"
    form_class=ClienteForm
    success_url=reverse_lazy("elim:cliente_list")
    success_message="Cliente creado satisfactoriamente"
    permission_required="elim.add_cliente"    

class ClienteEdit(VistaBaseEdit):
    permission_required="elim.change_cliente"
    model = Cliente
    template_name = "elim/cliente_form.html"
    context_object_name = "obj"
    form_class = ClienteForm
    success_url = reverse_lazy("elim:cliente_list")
    success_message = "Cliente actualizado satisfactoriamente"

class ClienteDel(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    permission_required="elim.delete_cliente"
    model = Cliente
    template_name ='elim/cliente_del.html'
    context_object_name ='obj'
    success_url = reverse_lazy("elim:cliente_list")
    success_message="Cliente eliminado satisfactoriamente"


@login_required(login_url="/login/")
@permission_required("elim.change_cliente",login_url="/login/")
def cliente_inactivar(request,id):
    cliente = Cliente.objects.filter(pk=id).first()
    print('cliente',cliente)
    if cliente:
        cliente.estado = not cliente.estado
        cliente.save()
        return redirect('elim:cliente_list')    
    return HttpResponse("FAIL")


# Bloque views Trayecto.

class TrayectoView(SinPrivilegios, generic.ListView):
    permission_required = "elim.view_trayecto"
    model = Trayecto
    template_name = "trayectos/trayecto_list.html"
    context_object_name = "obj"
    ordering = ['-id']

class TrayectoNew(VistaBaseCreate):
    model=Trayecto
    template_name="trayectos/trayecto_form.html"
    context_object_name="obj"
    form_class=TrayectoForm
    success_url=reverse_lazy("elim:reg_list")
    success_message="Trayecto creado satisfactoriamente"
    permission_required="elim.add_trayecto"
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        form.instance.direccion = str(form.instance.direccion).strip()
        return super().form_valid(form)

class TrayectoEdit(VistaBaseEdit):
    permission_required="elim.change_trayecto"
    model = Trayecto
    template_name = "trayecto/trayecto_form.html"
    context_object_name = "obj"
    form_class = TrayectoForm
    success_url = reverse_lazy("elim:reg_direccion_new")
    success_message = "Trayecto actualizado satisfactoriamente"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        form.instance.direccion = str(form.instance.direccion).strip()
        return super().form_valid(form)

@login_required(login_url="/login/")
@permission_required("elim.change_trayecto",login_url="/login/")
def direccion_inactivar(request,id):
    reg = Trayecto.objects.filter(pk=id).first()
    if reg:
        reg.estado = not reg.estado
        reg.save()
        return redirect('elim:trayecto_list')   
    return HttpResponse("FAIL")


# Bloque views Vehiculo.

class VehiculoView(SinPrivilegios, generic.ListView):
    permission_required = "elim.view_vehiculo"
    model = Vehiculo
    template_name = "vehiculos/vehiculo_list.html"
    context_object_name = "obj"
    ordering = ['placa','conductor']

class VehiculoNew(VistaBaseCreate):
    model=Vehiculo
    template_name="vehiculos/vehiculo_form.html"
    context_object_name="obj"
    form_class=VehiculoForm
    success_url=reverse_lazy("elim:vehiculo_list")
    success_message="Vehiculo creado satisfactoriamente"
    permission_required="elim.add_vehiculo" 

class VehiculoEdit(VistaBaseEdit):
    permission_required="elim.change_vehiculo"
    model = Vehiculo
    template_name = "vehiculos/vehiculo_form.html"
    context_object_name = "obj"
    form_class = VehiculoForm
    success_url = reverse_lazy("elim:vehiculo_new")
    success_message = "Vehiculo actualizado satisfactoriamente"

@login_required(login_url="/login/")
@permission_required("elim.change_vehiculo",login_url="/login/")
def vehiculo_inactivar(request,id):
    reg = Vehiculo.objects.filter(pk=id).first()
    if reg:
        reg.estado = not reg.estado
        reg.save()
        return redirect('elim:vehiculo_list')   
    return HttpResponse("FAIL")

# Bloque views proveedor.

class ProveedorView(SinPrivilegios, generic.ListView):
    permission_required = "elim.view_proveedor"
    model = Proveedor
    template_name = "elim/proveedor_list.html"
    context_object_name = "obj"

class ProveedorNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView):
    permission_required="elim.add_proveedor"
    model = Proveedor
    template_name="elim/proveedor_form.html"
    context_object_name = "obj"
    form_class=ProveedorForm
    success_url=reverse_lazy("elim:proveedor_list")
    success_message="Proveedor creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProveedorEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    permission_required="elim.change_proveedor"
    model = Proveedor
    template_name = "elim/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("elim:proveedor_list")
    success_message = "Proveedor actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ProveedorDel(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    permission_required="elim.delete_proveedor"
    model = Proveedor
    template_name ='elim/proveedor_del.html'
    context_object_name ='obj'
    success_url = reverse_lazy("elim:proveedor_list")
    success_message="Proveedor eliminado satisfactoriamente"
    

# crear registro

class RegistroView(SuccessMessageMixin, SinPrivilegios, generic.ListView):
    model = Registro
    template_name = "elim/reg_list.html"
    context_object_name = "obj"
    permission_required="elim.view_registro"
    ordering = ['-fecha']
    
    def get_queryset(self):        
        qs = super().get_queryset().filter(estado=True)      
        return qs


class RegistroNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView):
    permission_required="elim.add_registro"
    model=Registro
    template_name="elim/reg_form.html"
    context_object_name="obj"
    form_class=RegistroForm
    success_url=reverse_lazy("elim:reg_list")
    success_message="Servicio creado satisfactoriamente"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        #context = super().get_context_data(**kwargs)
        context = super(RegistroNew, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the Programador
        # context["fecha"] = datetime.datetime.today  
        context["clientes"] = Cliente.objects.all()
        context["trayectos"] = Trayecto.objects.filter(estado=True)    
        context["placas"] = Vehiculo.objects.all()
        context["solicitados_por"] = Persona.objects.all()        
        return context    

    def form_valid(self, form):
        form.instance.uc = User.objects.get(pk=self.request.user.id)
        return super().form_valid(form) 


class RegistroEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Registro
    template_name = "elim/reg_form.html"
    context_object_name = "obj"
    permission_required="elim.change_registro"
    form_class = RegistroForm
    success_url = reverse_lazy("elim:reg_list")
    success_message = "Servicio actualizado satisfactoriamente"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        # context = super().get_context_data(**kwargs)
        context = super(RegistroEdit, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the Programador        
        context["trayectos"] = Trayecto.objects.filter(estado=True)    
        context["placas"] = Vehiculo.objects.filter(estado=True)
        context["clientes"] = Cliente.objects.filter(estado=True)
        context["solicitados_por"] = Persona.objects.filter(estado=True)
        return context  
    
    def form_valid(self, form):        
        form.instance.um = self.request.user.id
        return super().form_valid(form)



@login_required(login_url='/login/')
@permission_required('elim.change_registro', login_url='bases:sin_privilegios')
def reg_add_edit(request,id=None):
    
    print('id---',id)
    #datetime.strptime(reg.fecha, '%d/%m/%Y %H:%i:%S'), #, datetime.date.isoformat(reg.fecha),
    context={
        'form': RegistroForm(),
        'clientes':Cliente.objects.filter(estado=True),
        'trayectos':Trayecto.objects.filter(estado=True), 
        'placas':Vehiculo.objects.filter(estado=True),
        'solicitados_por':Persona.objects.filter(estado=True),                
        'obj':{},
        'google_api_key' : settings.GOOGLE_API_KEY,
        'base_country':settings.BASE_COUNTRY
    }
    
    registro = {'fecha': datetime.now()}
    context ['obj'] = registro                        
    template_name = 'elim/reg_form.html'

    if request.method == 'GET':
        if id:
            reg = Registro.objects.filter(pk=id).first()
            if reg:                      
                registro = {
                    'id':reg.id,
                    'fecha': reg.fecha, 
                    'cliente':reg.cliente.id,                    
                    'placa':reg.placa,
                    'trayecto': reg.trayecto.id,
                    'solicitado_por':reg.solicitado_por.id,
                    'celular':reg.celular,
                    'medio_pago':reg.medio_pago,
                    'valor':reg.valor,
                    'costo':reg.costo,
                    'neto':reg.neto,
                    'um':reg.um,
                    'uc':reg.uc,
                }

                context ['form'] = RegistroForm(registro)
                context ['obj'] = registro                        
            
    if request.method == 'POST':
        reg_form = RegistroForm(request.POST)
        trayecto  = request.POST.get("trayecto")
        cliente = request.POST.get("cliente")
        placa = request.POST.get("placa")
        solicitado_por  = request.POST.get("solicitado_por")                
        reg = Registro.objects.filter(pk=id).first()
        registro = Registro()        
        if not id:
            registro = Registro (
                uc = User.objects.get(pk=request.user.id),                
                trayecto = Trayecto.objects.get(pk=trayecto),
                cliente = Cliente.objects.get(pk=cliente),
                placa = Vehiculo.objects.get(pk=placa),
                solicitado_por = Persona.objects.get(pk=solicitado_por),
                celular = request.POST.get("celular"),
                medio_pago = request.POST.get("medio_pago"),
                valor = request.POST.get("valor"),
                costo = request.POST.get("costo"),
                neto = request.POST.get("neto"), 
            )
            context ['obj'] = registro  
            if reg_form.is_valid():
                registro.save()
                messages.success(request,'Servicio creado')
                return redirect('elim:reg_list')
            else:
                messages.error(request, reg_form.errors)
        else:
            reg.um = request.user.id
            reg.fecha = datetime.strptime(request.POST.get("fecha") , '%d/%m/%Y %H:%M:%S')
            reg.trayecto = Trayecto.objects.get(pk=trayecto)
            reg.cliente = Cliente.objects.get(pk=cliente)
            reg.solicitado_por = Persona.objects.get(pk=solicitado_por)
            reg.placa = Vehiculo.objects.get(pk=placa)
            reg.celular = request.POST.get("celular")
            reg.medio_pago = request.POST.get("medio_pago")
            reg.valor = request.POST.get("valor")
            reg.costo = request.POST.get("costo")
            reg.neto = request.POST.get("neto")     
    
            context ['form']  = RegistroForm(instance=registro)
            context ['obj']  = reg
        
            if reg_form.is_valid():
                reg.save()
                messages.success(request,'Servicio actualizado')
                return redirect('elim:reg_list')
            else:
                print(reg_form.errors)
    return render(request,template_name,context)  

# Bloque views servicios.

class ServicioView(SinPrivilegios, generic.ListView):
    permission_required = "elim.view_servicio"
    model = Servicio
    template_name = "elim/servicio_list.html"
    context_object_name = "obj"

def servicio_new(request):
    placa =  Vehiculo.objects.all(),
    #placa = placa.filter(placa__icontains=name)
    template_name="elim/servicio_form.html"
    context={
        'form': ServicioForm(),
        'placa' : placa,
        "programador": Programador.objects.all(),
        "cliente" : Cliente.objects.all(),
        "trayecto" : Trayecto.objects.all(),
        "solicitado_por" : Persona.objects.all(),
    }
    return render(request, template_name, context)

class ServicioNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView):
    permission_required="elim.add_servicio"
    model = Servicio
    template_name="elim/servicio_form.html"
    context_object_name = "obj"
    form_class=ServicioForm
    success_url=reverse_lazy("elim:servicio_list")
    success_message="Servicio creado satisfactoriamente"    
    # def get_queryset(self):
    #     self.placa = get_object_or_404(Vehiculo, name=self.kwargs["placa"])
    #     return Vehiculo.objects.filter(placa=self.placa)

    # def get_queryset(self):
    #     self.programador = get_object_or_404(Programador, name=self.kwargs["programador"])
    #     return Programador.objects.filter(programador=self.programador)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        #context = super().get_context_data(**kwargs)
        context = super(ServicioNew, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the Programador
        context["fecha"] = datetime.datetime.today    
        context["placa"] = Vehiculo.objects.all()
        context["cliente"] = Cliente.objects.all()
        context["solicitado_por"] = Persona.objects.all()
        context["programador"] = Programador.objects.all()
        return context    

    def form_valid(self, form):        
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ServicioEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    permission_required="elim.change_servicio"
    model = Servicio
    template_name = "elim/servicio_form.html"
    context_object_name = "obj"
    form_class = ServicioForm
    success_url = reverse_lazy("elim:servicio_list")
    success_message = "Servicio actualizado satisfactoriamente"
    
    def get_object(self):
        obj = super().get_object()
        # Record the last fecha modificacion date
        obj.fm = timezone.now()
        obj.save()
        return obj
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        #context = super().get_context_data(**kwargs)
        context = super(ServicioEdit, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the Programador
        context["placa"] = Vehiculo.objects.all()
        context["cliente"] = Cliente.objects.all()
        context["solicitado_por"] = Persona.objects.all()
        context["programador"] = Programador.objects.all()

        return context
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print('***',form)
        return super().form_valid(form)

class ServicioDel(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    permission_required="elim.delete_servicio"
    model = Servicio
    template_name ='elim/servicio_del.html'
    context_object_name ='obj'
    success_url = reverse_lazy("elim:servicio_list")
    success_message="Servicio eliminado satisfactoriamente"

class MuseoCreateView(generic.CreateView):
    model = Museo
    template_name = "elim/add.html"
    form_class = MuseoForm
    success_url = '.'
    
    # def get_queryset(self):
    #     self.pais = get_object_or_404(Pais, name=self.kwargs["pais"])
    #     return
    # Pais.objects.filter(nombre=self.nombre)


def index(request):
    return render(request, "museo/index.html")


def index_js(request):
    
    return render(request, "museo/index_js.html")

def localizacion(request):
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ip_data['ip'])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    
    return render(request, "geo/geo.html", {'data':location_data})


class MuseoViewSet(viewsets.ModelViewSet):
    serializer_class = MuseoSerializer
    queryset = Museo.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['pais', 'id', "nombre"]
    search_fields = ["nombre"]
    ordering_fields = '__all__'

class PaisesViewSet(viewsets.ModelViewSet):
    serializer_class = PaisSerializer
    queryset = Pais.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', "nombre"]
    search_fields = ["nombre"]
    ordering_fields = '__all__'

class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', "nombre"]
    search_fields = ["nombre"]
    ordering_fields = '__all__'


class HomeTrayectosView(generic.ListView):
    template_name = "trayectos/home.html"
    context_object_name = 'data'
    model = Trayecto
    success_url = "/"
    ordering = ["-id"]   

class GeocodingView(View):
    template_name = "trayectos/home.html"
    
    def get(self,request,pk): 
        location = Trayecto.objects.get(pk=pk)

        if location.direccion and location.ciudad and location.zipcode and location.ciudad != None: 
            direccion_string = str(location.direccion)+", "+str(location.zipcode)+", "+str(location.ciudad)+", "+str(location.pais)

            gmaps = googlemaps.Client(key = settings.GOOGLE_API_KEY)
            result = gmaps.geocode(direccion_string)[0]
            
            location.lat = result.get('geometry', {}).get('location', {}).get('lat', None)
            location.lng = result.get('geometry', {}).get('location', {}).get('lng', None)
            location.place_id = result.get('place_id', {})
            location.um = request.user.id
            location.save()
            
            return redirect('elim:trayecto_view')

class ActInaTrayectoView(View):
    template_name = "trayectos/trayecto_list.html"
    
    def get(self,request,pk): 
        location = Trayecto.objects.get(pk=pk)
        location.estado = not location.estado
        location.um = request.user.id
        location.save()
            
        return redirect('elim:reg_direccion_new')

def rutas(request):

	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"base_country": settings.BASE_COUNTRY}
	return render(request, 'elim/route.html', context)

class MapView(View): 
    template_name = "trayectos/map.html"

    def get(self,request): 
        key = settings.GOOGLE_API_KEY
        eligable_locations = Locations.objects.filter(place_id__isnull=False)
        locations = []

        for a in eligable_locations: 
            data = {
                'lat': float(a.lat), 
                'lng': float(a.lng), 
                'name': a.name
            }

            locations.append(data)
        context = {
            "key":key, 
            "locations": locations
        }
        return render(request, self.template_name, context)

class DistanceView(View):
    template_name = "trayectos/distance.html"

    def get(self, request): 
        form = DistanceForm
        distances = Distances.objects.all()
        context = {
            'form':form,
            'distances':distances
        }

        return render(request, self.template_name, context)

    def post(self, request): 
        form = DistanceForm(request.POST)
        if form.is_valid(): 
            from_location = form.cleaned_data['from_location']
            from_location_info = Locations.objects.get(name=from_location)
            from_adress_string = str(from_location_info.adress)+", "+str(from_location_info.zipcode)+", "+str(from_location_info.city)+", "+str(from_location_info.country)

            to_location = form.cleaned_data['to_location']
            to_location_info = Locations.objects.get(name=to_location)
            to_adress_string = str(to_location_info.adress)+", "+str(to_location_info.zipcode)+", "+str(to_location_info.city)+", "+str(to_location_info.country)

            mode = form.cleaned_data['mode']
            now = datetime.now()

            gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
            calculate = gmaps.distance_matrix(
                    from_adress_string,
                    to_adress_string,
                    mode = mode,
                    departure_time = now
            )


            duration_seconds = calculate['rows'][0]['elements'][0]['duration']['value']
            duration_minutes = duration_seconds/60

            distance_meters = calculate['rows'][0]['elements'][0]['distance']['value']
            distance_kilometers = distance_meters/1000

            if 'duration_in_traffic' in calculate['rows'][0]['elements'][0]: 
                duration_in_traffic_seconds = calculate['rows'][0]['elements'][0]['duration_in_traffic']['value']
                duration_in_traffic_minutes = duration_in_traffic_seconds/60
            else: 
                duration_in_traffic_minutes = None

            
            obj = Distances(
                from_location = Locations.objects.get(name=from_location),
                to_location = Locations.objects.get(name=to_location),
                mode = mode,
                distance_km = distance_kilometers,
                duration_mins = duration_minutes,
                duration_traffic_mins = duration_in_traffic_minutes
            )

            obj.save()

        else: 
            print(form.errors)
        
        return redirect('elim:my_distance_view')

def route(request):

	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"base_country": settings.BASE_COUNTRY}
	return render(request, 'trayectos/route.html', context)