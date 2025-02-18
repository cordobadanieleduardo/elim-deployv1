from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import ClienteSerializer
from elim.models import Cliente

from django.db.models import Q

class ClienteList(APIView):
    def get(self,request):    
        return Response(ClienteSerializer(Cliente.objects.all(),many=True).data)