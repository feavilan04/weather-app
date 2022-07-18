from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class NombreDeporte(models.Model):
    deporte = models.CharField(max_length=100)
    
class Jugador(models.Model):
    deporte_que_practica = models.ForeignKey(NombreDeporte, on_delete=models.PROTECT)
    nombre_completo_jugador = models.CharField(max_length=20)


class Genero(models.Model):
    musica = models.CharField(max_length=25)

class Cantante(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    

class Estudiante(models.Model):
    primer_nombre = models.CharField(max_length=25)
    segundo_nombre = models.CharField(max_length=25)
    primer_apellido = models.CharField(max_length=25)
    segundo_apellido = models.CharField(max_length=25)

class Materias(models.Model):
    estudiante =models.ForeignKey(Estudiante, on_delete=models.PROTECT)
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
    documento = models.IntegerField()

class JuegosDeMesa(models.Model):
    jugadorm = models.ForeignKey(InscripcionJuegosMesa, on_delete=models.CASCADE)
    juegos_disponibles = models.CharField(max_length=40)


class AnimalesZoologico(models.Model): 
    nombre = models.CharField(max_length=25)
    lugar_de_origen = models.CharField(max_length=25)
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateField()


class Registro(models.Model):
    nombre_completo = models.CharField(max_length=25)
    documento = models.IntegerField()
    hora_de_llegada = models.TimeField()
    fecha = models.DateField()

class ObjetosEncontrados(models.Model):
    nombre_objeto = models.CharField(max_length=25)

class DescripcionDeObjetosEncontrados(models.Model):
    objeto = models.ForeignKey(ObjetosEncontrados, on_delete=models.PROTECT)
    descripcion_estado_de_objeto = models.TextField(max_length=200)
    

class Celulares(models.Model):
    marca_celular =models.CharField(max_length=25)

class Precios(models.Model):
    celular =models.ForeignKey(Celulares, on_delete=models.CASCADE)
    precios_sugeridos= models.URLField()


class Ventas(models.Model):
    producto =models.CharField(max_length=25)
    cantidad =models.IntegerField()
    hora_fecha=models.DateTimeField()

class VentaVideojuegos(models.Model):
    nombre_juego=models.CharField(max_length=45)
    precio =models.FloatField()

class VentaViajes(models.Model):
    destino = models.CharField(max_length=25)
    valor_viaje =models.FloatField()
    descuento = models.BooleanField()
    
class RegistroUsuario(models.Model):
    nombre_usuario=models.CharField(max_length=25)
    documento = models.IntegerField()

class RegistroUs(models.Model):
    usuario = models.ForeignKey(RegistroUsuario, on_delete=models.PROTECT)
    correo = models.EmailField()


class FechaCumpleannos(models.Model):
    nombre_completo = models.CharField(max_length=25)
    fecha= models.DateField()
    mensaje_cumple = models.TextField(max_length=200)

class Reservaciones(models.Model):
    nombres_completos =models.CharField(max_length=100)
    documento =models.IntegerField()
    fecha_reservacion =models.DateField()

class RegistroFormulario(models.Model):
    primer_nombre = models.CharField(max_length=25)
    segundo_nombre =models.CharField(max_length=25)
    primer_apellido =models.CharField(max_length=25)
    segundo_apellido=models.CharField(max_length=25)
    REGISTRO = 'R'
    TARJETA = 'TI'
    CEDULA = 'CC'
    TARJETAE = 'TE'
    CEDULAE = 'CE'
    PASAPORTE = 'PA'
    DOCUMENT_TYPE = [
        (REGISTRO, 'Registro'),
        (TARJETA, 'Tarjeta De Identidad'),
        (CEDULA, 'Cedula'),
        (TARJETAE, 'Tarjeta Extranjeria'),
        (CEDULAE, 'Cedula Extranjeria'),
        (PASAPORTE, 'Pasaporte'),
    ]
    document_type =models.CharField(
        max_length=25,
        choices=DOCUMENT_TYPE,
        default="R",    
    )
    numero_de_documento=models.IntegerField(max_length=25)
    correo=models.EmailField()
    