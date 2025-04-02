from rest_framework import serializers

from elim.models import Cliente, GastoConductor

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'

class GastoConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model=GastoConductor
        fields='__all__'