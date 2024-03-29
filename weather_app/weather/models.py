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


class BirthdayRegistrationForm(models.Model):
    first_name = models.CharField(max_length=25)
    second_name =models.CharField(max_length=25)
    first_surname  = models.CharField(max_length=25)
    second_surname =models.CharField(max_length=25)
    birth_day=models.DateField()
    city=models.CharField(max_length=25)
    CHINESE = 'CHI'
    DUTCH = 'DUT'
    ENGLISH = 'EN'
    FRENCH = 'FRE'
    GERMAN = 'GER'
    ITALIAN = 'ITA'
    JAPANESE = 'JAP'
    LATIN = 'LAT'
    NORWEGIAN = 'NOR'
    PORTUGUESE= 'POR'
    RUSSIAN = 'RUS'
    SPANISH = 'SPA'  
    THAI = 'THA'
    UKRAINIAN = 'UKR'
    VIETNAMESE = 'VIE'
    LANGUAGE = [
        (CHINESE, 'Chinese'),
        (DUTCH, 'Duth'),
        (ENGLISH, 'English'),
        (FRENCH, 'French'),
        (GERMAN, 'German'),
        (ITALIAN, 'Italian'),
        (JAPANESE, 'Japanese'),
        (LATIN, 'Latin'),
        (NORWEGIAN, 'Norwegian'),
        (PORTUGUESE, 'Portuguese'),
        (RUSSIAN, 'Rusian'),
        (SPANISH, 'Spanish'),
        (THAI, 'Thai'),
        (UKRAINIAN, 'Ukrainian'),
        (VIETNAMESE, 'Vietnamese'),
    ]
    language =models.CharField(
        max_length=25,
        choices=LANGUAGE,
        default="GER",    
    )
    message=models.TextField(max_length=200)


class NewRegistrationForm(models.Model):
    first_name = models.CharField(max_length=25)
    second_name =models.CharField(max_length=25)
    first_surname  = models.CharField(max_length=25)
    second_surname =models.CharField(max_length=25)
    city=models.CharField(max_length=25)


class Country(models.Model):
    country_name=models.CharField(max_length=25)
    telephone_indicative = models.IntegerField()

class Product(models.Model):
    country=models.ForeignKey(Country, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=25)
    barcode=models.CharField(max_length=30)
    technology=models.BooleanField()
   
class Department(models.Model):
    country=models.ForeignKey(Country, on_delete=models.CASCADE)
    department_name=models.CharField(max_length=25)
    population = models.IntegerField()


class FullCity(models.Model):
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    city_name=models.CharField(max_length=25)
    population = models.IntegerField()
    airport = models.BooleanField()

class Location(models.Model):
    city_location=models.ForeignKey(FullCity, on_delete=models.CASCADE)
    location_name=models.CharField(max_length=25)
    population = models.IntegerField()

class Neighborhood(models.Model):
    location_name=models.ForeignKey(Location, on_delete=models.CASCADE)
    neighborhood_name=models.CharField(max_length=25)
    population = models.IntegerField()

class President(models.Model):
    city_of_birth=models.ForeignKey(FullCity, on_delete=models.CASCADE)
    country=models.ForeignKey(Country, on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    date_of_birth = models.DateField()    