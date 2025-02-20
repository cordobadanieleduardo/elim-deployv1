from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django import forms
from .models import *

import datetime


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','estado']
        labels = {'nombre':"Nombre del cliente", 'estado':"Estado"}
        widget = {'nombre': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.queryset = Cliente.objects.filter(estado=True)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class TrayectoForm(forms.ModelForm):
    direccion = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput(
                                    attrs={'pattern' :"\\S(.*\\S)?" }))
    # ciudad = forms.CharField(max_length=20,initial='Bogotá', required=True)
    # pais = forms.CharField(max_length=20,initial='Colombia', required=True)
    zipcode = forms.CharField(initial='110110', required=True,max_length=6,
                                 widget=forms.TextInput(attrs={'max': "1000000",'min': "1000",'pattern':"[0-9]+" })
                                 )
    class Meta:
        model = Trayecto
        fields = ['direccion','ciudad','zipcode','pais','lat','lng','club']
        labels = {'direccion':'Dirección','estado':'Estado','zipcode':'Código postal','ciudad':'Ciudad','pais':'Pais','lat':'Latitud','lng':'Longitud','club':'Club'}
        # widget = {'direccion': forms.TextInput , 'zipcode': forms.NumberInput, }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        #self.queryset = Trayecto.objects.filter(estado=True)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
        self.fields['direccion'].widget.attrs['maxlength'] = 80 
        self.fields['pais'].widget.attrs['value'] = 'Colombia'
        self.fields['ciudad'].widget.attrs['value'] = 'Bogotá'
        self.fields['pais'].widget.attrs['readonly'] = 'true'
        # self.fields['zipcode'].widget.attrs['value'] = '110110'
        # self.fields['zipcode'].widget.attrs['max_length'] = 6
        # self.fields['zipcode'].widget.attrs['type'] = 'number'
        # self.fields['zipcode'].widget.attrs['max'] = '100000'
        
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','estado']
        labels = {'nombre':"Nombre del proveedor", 'estado':"Estado"}
        widget = {'nombre': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class MuseoForm(forms.ModelForm):
    class Meta:
        model = Museo
        fields = (
        'nombre',
        'pais',
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        # self.fields['pais'].query_set = Pais.objects.all()        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
        })


class RegistroForm(forms.ModelForm):
    #fecha = forms.DateTimeInput()
    #valor = forms.DecimalField(required=True)
    class Meta:
        model = Registro
        fields = ['fecha','trayecto','cliente','placa', 
                'solicitado_por','celular',
                'medio_pago','valor','costo','neto']
        exclude = ['um','fm','uc','fc','numero_registo']
        #widget={'trayecto': }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        #self.fields['pais'].query_set = Pais.objects.all()
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        #self.fields['cliente'].widget.attrs['required'] = True               

        self.fields['costo'].widget.attrs['readonly'] = True               
        self.fields['neto'].widget.attrs['readonly'] = True

class ServicioForm(forms.ModelForm):

    fecha = forms.DateField(initial=datetime.datetime.today)    
    # cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(estado=True))
    # placa = forms.ModelChoiceField(queryset=Vehiculo.objects.filter(estado=True))    
    # programador = forms.ModelChoiceField(queryset=Programador.objects.filter(estado=True))    
    # trayecto = forms.ModelChoiceField(queryset=Trayecto.objects.filter(estado=True))
    
    class Meta:
        model = Servicio
        fields = (
                  'fecha',
                  'cliente',
                  'placa',
                  'estado',
                  'trayecto',
                  'solicitado_por',
                  'celular',
                  'medio_pago',
                  'valor',  
                  'costo',
                  'neto',
                  'programador',
        )
        # exclude = (
        #            'um','fm','uc','fc',
        #           'estado',
        #           'numero_registo',
        #           'status',
        #           'cotizacion',
        #           'factura',
        #           'legalizado',
        # )
        # labels = {
        #           'fecha':"Fecha" ,
        #           'placa':"Placa",
        #           'estado':"Estado",
        #           'cliente':"Nombre del cliente",
        #           'medio_pago':"Medio de pago",
        #           'trayecto':"Dirección",
        #           'solicitado_por':"Solicitado por",
        #           'celular':"Numero de celular",
        #           'valor':"Valor",
        #           'costo':"Costo",
        #           'neto':"Neto",
        #           }
        # widgets = {
        #     'fecha': forms.DateInput(attrs={'class': 'form-control'}),
        #     # 'placa': forms.ChoiceField(choices=Vehiculo .objects.filter(estado=True)),
        #     'placa': AutocompleteSelect(
        #         Servicio._meta.get_field('placa').remote_field,
        #         admin.site,
        #         attrs={'placeholder':'seleccionar...'},
        #     )  ,
        #     'cliente': AutocompleteSelect(
        #         Servicio._meta.get_field('cliente').remote_field,
        #         admin.site,
        #         attrs={'placeholder':'seleccionar...'},
        #     ),
        #     'programador': AutocompleteSelect(
        #         Servicio._meta.get_field('programador').remote_field,
        #         admin.site,
        #         attrs={'placeholder':'seleccionar...'},
        #     ) ,
        #     'trayecto': AutocompleteSelect(
        #         Servicio._meta.get_field('trayecto').remote_field,
        #         admin.site,
        #         attrs={'placeholder':'seleccionar...'},
        #     )       
        # }
        
        
        # help_texts = {
        #     "name": _("Some useful help text."),
        # }
        # error_messages = {
        #     "name": {
        #         "max_length": _("This writer's name is too long."),
        #     },
        # }


    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
                    
        #self.fields['fecha'].widget.attrs['readonly'] = True
        # self.fields['fecha_'].widget.attrs['readonly'] = True
        # self.fields['fecha_factura'].widget.attrs['readonly'] = True
        # self.fields['sub_total'].widget.attrs['readonly'] = True
        # self.fields['descuento'].widget.attrs['readonly'] = True



# class SubCategoriaForm(forms.ModelForm):
#     categoria = forms.ModelChoiceField(
#         queryset=Categoria.objects.filter(estado=True)
#         .order_by('descripcion')
#     )
#     class Meta:
#         model=SubCategoria
#         fields = ['categoria','descripcion','estado']
#         labels = {'descripcion':"Sub Categoría",
#                "estado":"Estado"}
#         widget={'descripcion': forms.TextInput}

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args,**kwargs)
#         for field in iter(self.fields):
#             self.fields[field].widget.attrs.update({
#                 'class':'form-control'
#             })
#         self.fields['categoria'].empty_label =  "Seleccione Categoría"


# class MarcaForm(forms.ModelForm):
#     class Meta:
#         model=Marca
#         fields = ['descripcion','estado']
#         labels= {'descripcion': "Descripción de la Marca",
#                 "estado":"Estado"}
#         widget={'descripcion': forms.TextInput()}

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in iter(self.fields):
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control'
#             })


# class UMForm(forms.ModelForm):
#     class Meta:
#         model=UnidadMedida
#         fields = ['descripcion','estado']
#         labels= {'descripcion': "Descripción de la Marca",
#                 "estado":"Estado"}
#         widget={'descripcion': forms.TextInput()}

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in iter(self.fields):
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control'
#             })


# class ProductoForm(forms.ModelForm):
#     class Meta:
#         model=Producto
#         fields=['codigo','codigo_barra','descripcion','estado', \
#                 'precio','existencia','ultima_compra',
#                 'marca','subcategoria','unidad_medida','foto']
#         exclude = ['um','fm','uc','fc']
#         widget={'descripcion': forms.TextInput()}

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in iter(self.fields):
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control'
#             })
#         self.fields['ultima_compra'].widget.attrs['readonly'] = True
#         self.fields['existencia'].widget.attrs['readonly'] = True










modes = (
    ("driving", "driving"), 
    ("walking", "walking"),
    ("bicycling", "bicycling"),
    ("transit", "transit")
)

class DistanceForm(forms.ModelForm): 
    from_location = forms.ModelChoiceField(label="Location from", required=True, queryset=Locations.objects.all())
    to_location = forms.ModelChoiceField(label="Location to", required=True, queryset=Locations.objects.all())
    mode = forms.ChoiceField(choices=modes, required=True)
    class Meta: 
        model = Distances
        exclude = ['created_at', 'edited_at', 'distance_km','duration_mins','duration_traffic_mins']