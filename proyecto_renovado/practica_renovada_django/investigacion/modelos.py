from django.db import models

# Definición del modelo Laboratorio
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

# Definición del modelo DirectorGeneral
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE, related_name='director_general')
    especialidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.laboratorio.nombre})"

# Definición del modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='productos')
    anio_fabricacion = models.IntegerField()
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

