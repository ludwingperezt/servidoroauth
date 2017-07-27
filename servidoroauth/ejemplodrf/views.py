from django.shortcuts import render
from ejemplodrf import models
from ejemplodrf.serializers import *

from rest_framework import serializers, viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, IsAuthenticatedOrTokenHasScope

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    #Se especifica que para acceder a este endpoint, el token debe tener un scope de lectura/escritura
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ['productos']
