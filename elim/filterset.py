import django_filters
from .views import GastoConductor
from distutils.util import strtobool

from .models import Medio_pago

class GastoConductorFilter(django_filters.FilterSet):
    fecha = django_filters.IsoDateTimeFromToRangeFilter()
    # fecha = django_filters.IsoDateTimeFilter(lookup_expr='gt')   
    factura = django_filters.CharFilter(lookup_expr='icontains')
    # medio_pago = django_filters.TypedChoiceFilter(choices=Medio_pago, coerce=strtobool )
    # medio_pago = django_filters.ModelChoiceFilter()  #(choiceFilter= Medio_pago)

    class Meta:        
        model = GastoConductor
        fields =['fecha','factura']
        
        # fields = {            
        #     # 'fecha': ['fecha__gt'],
        #     'factura':['icontains'],
        #     # 'medio_pago':['exact', 'fecha__gt'],            
        # }
    
    # @property
    # def qs(self):
    #     parent = super().qs
    #     medio_pago = getattr(self.request, 'medio_pago', None)
    #     return parent.filter(estado=True) | parent.filter(medio_pago__contains=medio_pago)