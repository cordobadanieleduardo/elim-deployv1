from rest_framework import serializers

from .models import Museo,Pais,Cliente

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
