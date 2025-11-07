from django.db import models

class Empresa(models.TextChoices):
    VERFRUT = 'VERFRUT', 'VERFRUT'
    RAPEL = 'RAPEL', 'RAPEL'

class Asistencia(models.Model):
    dni = models.CharField(max_length=20)
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    horas_trabajadas = models.CharField(max_length=50)
    mes = models.CharField(max_length=20)
    empresa = models.CharField(max_length=20, choices=Empresa.choices)

    class Meta:
        unique_together = ('dni', 'fecha', 'empresa')
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.nombre} - {self.fecha} ({self.empresa})"
