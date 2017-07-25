from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Productos(models.Model):
    codigo = models.CharField(db_column='codigo', max_length=10, blank=True, null=True)
    nombre = models.CharField(db_column='nombre', max_length=255, blank=True, null=True)
    precio = models.DecimalField(db_column='precio', max_digits=9, decimal_places=2, blank=True, null=True)
    existencia = models.DecimalField(db_column='existencia', max_digits=9, decimal_places=3, blank=True, null=True)
