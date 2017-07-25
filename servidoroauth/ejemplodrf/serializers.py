from rest_framework import serializers
from ejemplodrf.models import *
from ejemplodrf.views import *

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ('id',
            'codigo',
            'nombre',
            'precio',
            'existencia')
