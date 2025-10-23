from django.db import models

#Categorías y estados de los equipos
CATEGORIAS_EQUIPO = [
    ('PROY', 'Proyector'),
    ('NOTE', 'Notebook'),
    ('IMPR', 'Impresora'),
]

ESTADOS_EQUIPO = [
    ('OP', 'Operativo'),
    ('REP', 'En reparación'),
    ('BAJ', 'Dado de baja'),
]

#Modelo de los equipos

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=5, choices=CATEGORIAS_EQUIPO)
    estado = models.CharField(max_length=3, choices=ESTADOS_EQUIPO)
    fecha_ingreso = models.DateField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.get_categoria_display()} ({self.get_estado_display()})"
