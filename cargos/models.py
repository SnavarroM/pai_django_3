from django.db import models

class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=50, verbose_name="Descripción Cargo")
    estado = models.BooleanField(default=True, verbose_name="Estado")  


    def __str__(self):
        return self.nombre_cargo
