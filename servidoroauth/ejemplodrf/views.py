from django.shortcuts import render
from rest_framework import viewsets
from ejemplodrf import models
from ejemplodrf.serializers import *


from rest_framework import permissions, routers, serializers, viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    #Se especifica que para acceder a este endpoint, el token debe tener un scope de lectura/escritura
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
