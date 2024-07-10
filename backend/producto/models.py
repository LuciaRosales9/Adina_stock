from django.db import models

from django.db import models
from django.core.exceptions import ValidationError
import datetime
from django.contrib.auth.hashers import make_password, check_password

class Talle(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__ (self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Talles"
        app_label = 'producto'
    def clean(self):
        if not self.nombre:
            raise ValidationError("El campo 'Nombre' no puede estar vacío.")

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)  # Hacer el campo opcional
    def __str__ (self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Categorías"
        app_label = 'producto'
    def clean(self):
        if not self.nombre:
            raise ValidationError("El campo 'Nombre' no puede estar vacío.")   


class Producto(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255,  blank=True, null=True)  # Hacer el campo opcional
    costo = models.DecimalField (max_digits=10, decimal_places=2)
    porcentajeVenta = models.DecimalField (max_digits=10, decimal_places=2)
    stock = models.DecimalField (max_digits=10, decimal_places=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    talle = models.ForeignKey(Talle, on_delete=models.CASCADE)
    def __str__ (self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Productos"
        app_label = 'producto'
    def clean(self):
        if not self.nombre:
            raise ValidationError("El campo 'Nombre' no puede estar vacío.")
        if not self.codigo:
            raise ValidationError("El campo 'Código' no puede estar vacío.")
        if not self.costo:
            raise ValidationError("El campo 'Costo' no puede estar vacío.")
        if not self.stock:
            raise ValidationError("El campo 'Stock' no puede estar vacío.")
        if not self.porcentajeVenta:
            raise ValidationError("El campo 'Porcentaje para la Venta' no puede estar vacío.")
        

