from rest_framework import serializers

from .models import Museo,Pais,Cliente,GastoConductor

class MuseoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Museo
        fields='__all__'


class PaisSerializer(serializers.ModelSerializer):

    class Meta:
        model=Pais
        fields='__all__'


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model= Cliente
        fields='__all__'


class GastoConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model= GastoConductor
        fields='__all__'