from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField


# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    """ Modelo para tabla persona """
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrativo'),
        ('2', 'Economista'),
        ('3', 'Otro')
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres completos',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField(blank=True, null=True)

    # Ordena el admin de django respecto a la visualización (Nombres, orden etc).
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['last_name']
        unique_together = ('first_name', 'last_name')  #impide que se registre una combinacion igual de ambos campos.

    def __str__(self):
        #return self.first_name + ' ' + self.last_name
        return str(self.id) + '-' + self.first_name + '-' + self.last_name

