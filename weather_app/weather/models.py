from re import M
from statistics import mode
from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

class Deporte(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.PROTECT)
    deporte_practica = models.CharField(max_length=100)


class Cantante(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)

class Genero(models.Model):
    cantante = models.CharField(Cantante, on_delete=models.CASCADE)
    generom = models.CharField(max_length=25)
    

class Estudiante(models.Model):
    primer_nombre = models.CharField(max_length=25)
    segundo_nombre = models.CharField(max_length=25)
    primer_apellido = models.CharField(max_length=25)
    segundo_apellido = models.CharField(max_length=25)

class Materias(models.Model):
    estudiante =models.CharField(Estudiante, on_delete=models.PROTECT)
    grado =models.CharField(max_length=25)
    materias_reprobadas = models.IntegerField()

class PersonasViaje(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    destino = models.CharField(max_length=25)
    plata_abonada = models.IntegerField()


class InscripcionJuegosMesa(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    documento = models.IntegerField(max_length=25)

class JuegosDeMesa(models.Model):
    jugadorm = models.CharField(InscripcionJuegosMesa, on_delete=models.CASCADE)
    juegos_disponibles = models.CharField(max_length=40)


class AnimalesZoologico(models.Model): 
    nombre = models.CharField(max_length=25)
    lugar_de_origen = models.CharField(max_length=25)
    cantidad = models.IntegerField(max_length=25)
    fecha_ingreso = models.DateField()


class Registro(models.Model):
    nombre_completo = models.CharField(max_length=25)
    documento = models.IntegerField()
    hora_de_llegada = models.TimeField()
    fecha = models.DateField()

class ObjetosEncontrados(models.Model):
    nombre_objeto = models.CharField(max_length=25)

class DescripcionDeObjetosEncontrados(models.Model):
    objeto = models.CharField(ObjetosEncontrados, on_delete=models.PROTECT)
    descripcion_estado_de_objeto = models.TextField(max_length=200)
    


