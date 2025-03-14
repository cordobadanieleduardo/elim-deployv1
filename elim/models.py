from django.core.validators import MaxValueValidator, MinValueValidator
# from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
#from django_userforeignkey.models.fields import UserForeignKey
import uuid
from bases.models import ClaseModelo, ClaseModelo2

# Trayecto models.
class Trayecto(ClaseModelo):
    
    direccion = models.CharField(verbose_name='Dirección',max_length=200)    
    zipcode = models.CharField(verbose_name='Código postal',max_length=6)
    ciudad = models.CharField(verbose_name='Ciudad',max_length=200,blank=True, null=True)
    pais = models.CharField(verbose_name='Pais',max_length=200,blank=True, null=True)
    lat = models.CharField(verbose_name='Latitud',max_length=200,blank=True, null=True)
    lng = models.CharField(verbose_name='Longitud',max_length=200,blank=True, null=True)
    club = models.CharField(verbose_name='Club',max_length=500,blank=True, null=True)    
    place_id = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return f'{self.direccion}'
        # return '{}'.format(self.direccion)
    
    def save(self):
        super(Trayecto,self).save()

    class Meta:
        verbose_name_plural = 'Trayectos'

# Create your models here.

class Persona(ClaseModelo):
    nombre = models.CharField(max_length=50,help_text= "Nombre de la persona")
    celular = models.CharField(max_length=10,help_text= "Número de celular")
    
    def __str__(self):
        # return '{}'.format(self.nombre)
         return f'{self.nombre}'
    
    def save(self):
        super(Persona,self).save()

    class Meta:
        verbose_name_plural = 'Personas'

class Cliente(ClaseModelo):
    nombre = models.CharField(max_length=50,help_text= "Nombre del cliente")
    
    def __str__(self):
        # return '{}'.format(self.nombre)
        return f'{self.nombre}'
    
    def save(self):
        super(Cliente,self).save()

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Clientes'
        

class Proveedor(ClaseModelo):
    nombre = models.CharField(max_length=50,help_text= "Nombre del proveedor")
    
    def __str__(self):
        # return '{}'.format(self.nombre)
        return f'{self.nombre}'
    
    def save(self):
        super(Proveedor,self).save()

    class Meta:
        verbose_name_plural = 'Proveedores'

class Conductor(ClaseModelo):
    cedula = models.BigIntegerField(help_text= "Cédula",blank=True,null=True)
    nombre = models.CharField(max_length=50,help_text= "Nombre del conductor")

    def __str__(self):
        # return '{}'.format(self.nombre)
        return f'{self.nombre}'
    
    def save(self):
        super(Conductor,self).save()

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Conductores'

class Vehiculo(ClaseModelo):
    
    class Disponibilidad(models.TextChoices):
        INACTIVO = "INACTIVO", _("Inactivo")
        ACTIVO = "ACTIVO", _("Activo")
        VERDE = "VERDE", _("Verde")
        ROJO = "ROJO", _("Rojo")
    
    class Tipo(models.TextChoices):
        VAN = "VAN", _("Van")
        ESTACAS = "ESTACAS", _("Estacas")
        MINIVAN = "MINIVAN", _("Minivan")
        CAMION = "CAMION", _("Camion")
    
    tipo = models.CharField(max_length=10,choices=Tipo,default=Tipo.VAN)
    placa = models.CharField(primary_key = True,max_length=6)    
    conductor = models.ForeignKey(Conductor,on_delete=models.PROTECT,max_length=50)    
    hora = models.DateTimeField()
    disponibilidad = models.CharField(max_length=10,choices=Disponibilidad,default=Disponibilidad.INACTIVO)
    mecanico = models.BooleanField(default=False)
    restaurante = models.BooleanField(default=False)
    enfermo = models.BooleanField(default=False)
    ubicacion = models.ForeignKey(Trayecto,on_delete=models.RESTRICT,blank=True, null=True)


    def is_upperclass(self):
        return self.disponibilidad in {
            self.Disponibilidad.ACTIVO,
            self.Disponibilidad.INACTIVO,
        }

    def __str__(self):
        return f'{self.placa}'
    
    def save(self):
        super(Vehiculo,self).save()

    class Meta:
        verbose_name_plural = 'Vehiculos'


class Programador(ClaseModelo):
    nombre = models.CharField(max_length=50,help_text= "Nombre del programador")

    def __str__(self):
        # return '{}'.format(self.nombre)
        return f'{self.nombre}'
    
    def save(self):
        super(Programador,self).save()

    class Meta:
        verbose_name_plural = 'Programadores'


class Servicio(ClaseModelo):
    
    class Medio_pago(models.TextChoices):
        CONTADO = "CONTADO", _("Contado")
        CREDITO = "CREDITO", _("Crédito")
        TRANSFERENCIA = "TRANSFERENCIA", _("Transferencia")

    class Status(models.TextChoices):
        Creado = "creado", _("Creado")        
        Ejecutado = "ejecutado", _("Ejecutado")
        Cotizado = "cotizado", _("Cotizado")
        Facturado = "facturado", _("Facturado")
        no_show = "no_show", _("NO SHOW")
    
    class Legalizado(models.TextChoices):        
        sin_legalizar = "sin legalizar", _("Sin legalizar")
        Legalizado = "legalizado", _("Legalizado")

    fecha = models.DateTimeField(null=True,blank=True)
    numero_registo = models.UUIDField(default=uuid.uuid4,max_length=80)
    cliente	 = models.ForeignKey(Cliente,on_delete=models.CASCADE,max_length=50,)
    placa = models.ForeignKey(Vehiculo,on_delete=models.CASCADE,)
    medio_pago = models.CharField(verbose_name='Medio de peago',max_length=15,choices=Medio_pago,default=Medio_pago.CONTADO,)
    valor = models.DecimalField(max_digits=9, decimal_places=2,default=0.0)
    trayecto = models.ForeignKey(Trayecto,on_delete=models.CASCADE,max_length=50,)
    solicitado_por = models.ForeignKey(Persona,on_delete=models.CASCADE,)
    celular = models.CharField(max_length=10,)
    programador = models.ForeignKey(Programador,on_delete=models.CASCADE,)
    costo = models.DecimalField(max_digits=9, decimal_places=2 ,default=0.0)
    neto = models.DecimalField(max_digits=9, decimal_places=2,default=0.0)
    status = models.CharField(max_length=15,choices=Status,default=Status.Creado,help_text= "Status")
    cotizacion = models.DecimalField(max_digits=9, decimal_places=2,default=0,blank=True)
    factura = models.CharField(blank=True,max_length=50,help_text= "Factura")
    legalizado = models.CharField(max_length=15,choices=Legalizado,default=Legalizado.sin_legalizar,help_text= "Legalizado")
    
    def __str__(self):
        # return '{}'.format(self.placa)
        return f'{self.placa}'
    
    def save(self):
        super(Servicio,self).save()

    class Meta:
        verbose_name_plural = 'Servicios'
        #unique_together = ('fecha','cliente','cliente','medio_pago','valor','trayecto')


class Pais(models.Model):
    nombre = models.CharField('Nombre Pais',max_length=50)
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
    
    def __str__(self):
        return self.nombre


class Museo(models.Model):
    nombre = models.CharField('Nombre Museo',max_length=80)
    pais = models.ForeignKey('Pais',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Museo'
        verbose_name_plural = 'Museos'
    
    def __str__(self):
        return self.nombre

class Parametro(ClaseModelo2):      
    nombre = models.CharField(max_length=200,null=False,blank=False)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self):
        return f'{self.nombre}={self.valor} '

    class Meta:
        verbose_name_plural = 'Parametros'
class Medio_pago(models.TextChoices):
        CONTADO = "CONTADO", _("Contado")
        CREDITO = "CREDITO", _("Crédito")
        TRANSFERENCIA = "TRANSFERENCIA", _("Transferencia")
class Registro(ClaseModelo):
    
    numero_registo = models.UUIDField(default=uuid.uuid4,max_length=80)    
    fecha = models.DateTimeField(null=True,blank=True)
    direccion = models.CharField(max_length=200,null=False,blank=False)
    latitud = models.CharField(max_length=200,null=True,blank=True)
    longitud = models.CharField(max_length=200,null=True,blank=True)
    trayecto = models.ForeignKey(Trayecto,on_delete=models.PROTECT)
    cliente	= models.ForeignKey(Cliente,on_delete=models.PROTECT)    
    placa = models.ForeignKey(Vehiculo,on_delete=models.PROTECT)    
    solicitado_por = models.ForeignKey(Persona,on_delete=models.PROTECT)
    celular = models.CharField(max_length=10)
    medio_pago = models.CharField(max_length=15,choices=Medio_pago,default=Medio_pago.CONTADO)
    valor = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)
    costo = models.DecimalField(max_digits=9, decimal_places=2, default=0.0,blank=True)
    neto = models.DecimalField(max_digits=9, decimal_places=2, default=0.0,blank=True)
    efectivo = models.DecimalField(max_digits=9, decimal_places=2,default=0.0,blank=True)
    credito = models.DecimalField(max_digits=9, decimal_places=2,default=0.0,blank=True)
    transferencia = models.DecimalField(max_digits=9, decimal_places=2,default=0.0,blank=True)
    porcentaje = models.DecimalField(max_digits=9, decimal_places=2,default=0.0,blank=True)
    def __str__(self):
        return f"{self.direccion}, {self.placa}"        
        # return "%s %s" % (self.direccion, self.placa)        
        # return f'{self.placa}'
        # return '{}'.format(self.placa)
    
    def save(self):        
        self.porcentaje = Parametro.objects.get(pk=1).valor
        self.costo = float(self.valor) * float(self.porcentaje) or 0.25
        self.neto = float(self.valor) - float(self.costo)
        if self.medio_pago == Medio_pago.CONTADO:
            self.credito = float(0)
            self.transferencia = float(0)
            self.efectivo = float(self.valor)
        elif self.medio_pago == Medio_pago.CREDITO:
            self.credito = float(self.valor)
            self.transferencia = float(0)
            self.efectivo = float(0)
        elif self.medio_pago == Medio_pago.TRANSFERENCIA:
            self.credito = float(0)
            self.transferencia = float(self.valor)        
            self.efectivo = float(0)
        super(Registro,self).save()

    class Meta:
        verbose_name_plural = 'Registros'


class Locations(models.Model):
    club = models.CharField(verbose_name='Club',max_length=500,blank=True, null=True)
    name = models.CharField(verbose_name='Nombre',max_length=500)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(verbose_name='Ciudad',max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    adress = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)
    lat = models.CharField(max_length=200,blank=True, null=True)
    lng = models.CharField(max_length=200,blank=True, null=True)
    place_id = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.name

class Distances (models.Model): 
    from_location = models.ForeignKey(Locations, related_name = 'from_location', on_delete=models.CASCADE)
    to_location = models.ForeignKey(Locations, related_name = 'to_location', on_delete=models.CASCADE)
    mode = models.CharField(max_length=200, blank=True, null=True)
    distance_km = models.DecimalField(max_digits=10, decimal_places=2)
    duration_mins = models.DecimalField(max_digits=10, decimal_places=2)
    duration_traffic_mins = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

class PerfilConductor(models.Model):
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    
    def __str__(self):
        # return '{}'.format(self.vehiculo)    
        return f'{self.vehiculo}'
    class Meta:
        verbose_name_plural = 'Perfil de conductores'



class GastoConductor(ClaseModelo):    
    class Concepto(models.TextChoices):
        GASOLINA = "gasolina", _("Gasolina")
        PEAJE = "peaje", _("Peajes")
        OTRO = "otro", _("Otro")
    
    class Medio(models.TextChoices):
        CONTADO = "efectivo", _("Efectivo")
        CREDITO = "chip", _("Chip")

    numero_registro = models.UUIDField(default=uuid.uuid4,max_length=80)    
    fecha = models.DateTimeField(blank=True, null=True)
    concepto = models.CharField(max_length=15,choices=Concepto,default=Concepto.GASOLINA)
    medio_pago = models.CharField(max_length=15,choices=Medio,default=Medio.CONTADO)
    valor = models.DecimalField(max_digits=9,decimal_places=2,default=0.0,
        validators=[MaxValueValidator(1000000), MinValueValidator(10000)])
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.RESTRICT)
    placa = models.CharField(max_length=6)
    cedula = models.IntegerField()
    conductor = models.CharField(blank=True,max_length=200)
    imagen = models.ImageField(upload_to="gastos")

    def __str__(self):
        return f'{self.fecha}'
    
    class Meta:
        verbose_name_plural = 'Gastos del conductor'
        
    def save(self):
        self.placa = self.placa.upper()
        return super().save()
    

class Viaje(models.Model): 
    from_location = models.ForeignKey(Trayecto, related_name = 'from_location', on_delete=models.CASCADE)
    to_location = models.ForeignKey(Registro, related_name = 'to_location', on_delete=models.CASCADE)
    mode = models.CharField(max_length=200, blank=True, null=True)
    distance_km_text = models.CharField(max_length=20, blank=True, null=True)
    distance_km = models.DecimalField(max_digits=10, decimal_places=2)
    duration_mins_text = models.CharField(max_length=20, blank=True, null=True)
    duration_mins = models.DecimalField(max_digits=10, decimal_places=2)
    duration_traffic_mins_text = models.CharField(max_length=20, blank=True, null=True)
    duration_traffic_mins = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id