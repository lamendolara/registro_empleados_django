from django.db import models

# Create your models here.


class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    # Ordena el admin de django respecto a la visualización (Nombres, orden etc.
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        unique_together = ('name', 'shor_name')  #impide que se registre una combinacion igual de ambos campos.

    def __str__(self):
        return str(self.id) + '-' + self.name



