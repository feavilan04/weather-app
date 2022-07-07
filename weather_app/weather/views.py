import datetime
from multiprocessing import context
import random
import time
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .models import AnimalesZoologico, Cantante, Celulares, City, DescripcionDeObjetosEncontrados, Estudiante, FechaCumpleannos, InscripcionJuegosMesa, JuegosDeMesa, Jugador, Materias, NombreDeporte, Genero, ObjetosEncontrados, PersonasViaje, Precios, Registro, RegistroUs, RegistroUsuario, Reservaciones, VentaViajes, VentaVideojuegos, Ventas
from .forms import CityForm
from django.views import View
import random
# Create your views here.
class IndexPrueba(View):
    def get(self, request):
        names = [
            'juan',
            'carlos',
            'pepe',
            'jose']
        name = names[random.randint(0, len(names) - 1)]
        context = {
            'nombre_seleccionado':name
        }
        return render(request, 'weather/vista1.html',context)
    

class VistaDos(View):
    def get(self, request):
        num = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10]
        nume = num[random.randint(0, len(num) - 1)]
        context = {
            'numero_seleccionado':nume
        }
        return render(request, 'weather/vista2.html', context)
    

class VistaTres(View):
    def get(self, request):
        start = datetime.date(2021,12,10)
        periods = 5
        daterange = []
        for day in range(periods):
            date = (start + datetime.timedelta(days = day)).isoformat()
            daterange.append(date)
        context={
            'fecha':daterange
        }
        return render(request, 'weather/vista3.html', context)

class VistaCuatro(View):
    def get(self, request):
        precios = [
            50,
            75,
            46,
            22,
            80,
            65,
            8]
        min = max = precios[0]
        for precio in precios:
            if precio < min:
                min = precio
            elif precio > max:
                max = precio
        
        context = {

            'numero_minimo':min, 
            'numero_maximo':max
        }
        return render(request, 'weather/vista4.html', context)


class VistaCinco(View):
    def get(self,request):
        palabra = "murcielago"
        vocales = {
                'a':0,
                'e':0, 
                'i':0, 
                'o':0, 
                'u':0
                }
        for vocal, recurrencia in vocales.items(): 
            for letra in palabra: 
                if letra == vocal:
                    recurrencia += 1
            vocales[vocal] = recurrencia
        context={

            'vocal':vocales
        }
        return render(request, 'weather/vista5.html', context)

    

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'
    err_msg = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city, settings.OPENWEATHER_API_KEY)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'la ciudad no existe !'
            else:
                err_msg = 'la ciudad ya existe!'
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'Ciudad añadida con éxito!'
            message_class = 'is_success'
    
    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city, settings.OPENWEATHER_API_KEY)).json()
        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = {
        'weather_data' : weather_data, 
        'form' : form,
        'message' : message,
        'message_class' : message_class
        }
    return render(request,'weather/weather.html', context)

def delete_city(requests, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')

class Prueba(View):
    def get(self,request):
        hora = time.strftime('%H')
        hora_integer = int(hora)

        hora_completa = time.strftime('%H:%M:%S (%Z)')
        fecha_completa = time.strftime('%d %b %Y')
        saludo = ""

        if hora_integer < 12: # verdadero para todas las horas entre 00 y 11
            saludo = "Buenos días"
        elif hora_integer < 19: # verdadero para todas la horas entre 12 y 18
            saludo = "Buenas tardes"
        else: # la hora debe ser mayor a 18
            saludo = "Buenas Noches"
        mensaje = "{0} son las : {1}".format(saludo, hora_completa)
        mensaje_formateo = "{primer_valor} son las : {segundo_valor} del {tercer_valor}".format(primer_valor=saludo, segundo_valor=hora_completa, tercer_valor=fecha_completa)
        return HttpResponse(mensaje_formateo)

class SampleView(View):
    def get(self,request):
        names = [
            'John',
            'Paul',
            'George',
            'Ringo',
            'Pete',
            'Stuart',
            'Brian',
            'Ron',
            'Jim',
            'Bill',
            'Jack',
            'Joe',
            'Mike',
            'Tom',
            'Dick',
            'Harry',
            'Larry',
            'Joe',
            'John',
            'Paul',
            'George',
            'Ringo',
            'Pete',
            'Stuart',
            'Brian',
            'Ron',
            'Jim',
            'Bill',
            'Jack',
            'Joe',
            'Mike',
            'Tom',
            'Dick',
            'Harry',
            'Larry']
        # pick one of these randomly
        name = names[random.randint(0, len(names) - 1)] # numero entre 0 y 19
        context = {
            'nombre_seleccionado': name,
            'cantidad_de_nombres': len(names),
            'lista_nombres': names
        }
        return render(request, 'weather/sample_template.html', context) 

class VistaPrueba(View):     
    def get(self, request):
        return HttpResponse('Esta es una prueba vista')
    
    def post(self, request):
        print(request.POST)
    
class InsercionModelos(View):
    def get(self, request):
        nombre_deporte = NombreDeporte()
        nombre_deporte.deporte="futbol"
        nombre_deporte.save()

        leonel_messi = Jugador()
        leonel_messi.deporte_que_practica=nombre_deporte
        leonel_messi.nombre_completo_jugador="Leonel Messi"
        leonel_messi.save()


        genero = Genero()
        genero.musica="Salsa"
        genero.save()

        nombrecantante = Cantante()
        nombrecantante.genero=genero
        nombrecantante.nombre="Maelo"
        nombrecantante.apellido="Ruiz"
        nombrecantante.save()

        estudiante = Estudiante()
        estudiante.primer_nombre="Luis"
        estudiante.segundo_nombre="Carlos"
        estudiante.primer_apellido="Parra"
        estudiante.segundo_apellido="Cepeda"
        estudiante.save()

        materia_reprobada=Materias()
        materia_reprobada.estudiante=estudiante
        materia_reprobada.grado="Once"
        materia_reprobada.materias_reprobadas=3   


        persona_viaje= PersonasViaje()
        persona_viaje.nombre="Julio"
        persona_viaje.apellido= "Perez"
        persona_viaje.destino="Medellin"
        persona_viaje.plata_abonada= 2000000
        persona_viaje.save()


        inscripcionjuegosmesa = InscripcionJuegosMesa()
        inscripcionjuegosmesa.nombre="Camilo"
        inscripcionjuegosmesa.apellido="Herrera"
        inscripcionjuegosmesa.documento= 2588452254
        inscripcionjuegosmesa.save()

        juegomesa=JuegosDeMesa()
        juegomesa.jugadorm=inscripcionjuegosmesa
        juegomesa.juegos_disponibles= 2
        juegomesa.save()



        animaleszoologico = AnimalesZoologico()
        animaleszoologico.nombre="Leon"
        animaleszoologico.lugar_de_origen="La Selva"
        animaleszoologico.cantidad= 2
        animaleszoologico.fecha_ingreso= datetime.date(2022, 5, 20)
        animaleszoologico.save()



        regitro = Registro()
        regitro.nombre_completo = "Felipe Vera"
        regitro.documento = 123258561
        regitro.hora_de_llegada = datetime.time(6,30,00)
        regitro.fecha = datetime.date(2022, 5, 20)
        regitro.save()


        objetosencontrados = ObjetosEncontrados()
        objetosencontrados.nombre_objeto="silla"
        objetosencontrados.save()

        busqueda_objetos = DescripcionDeObjetosEncontrados()
        busqueda_objetos.objeto=objetosencontrados
        busqueda_objetos.descripcion_estado_de_objeto="Se ecuentra sin una pata"
        busqueda_objetos.save()



        celular = Celulares()
        celular.marca_celular="SAMSUNG"
        celular.save()

        valorsugerido = Precios()
        valorsugerido.celular=celular
        valorsugerido.precios_sugeridos="https://shop.samsung.com.co"

        ventas =Ventas()
        ventas.producto="azucar"
        ventas.cantidad= 2
        ventas.hora_fecha= datetime.datetime(2022, 5, 20, 00,00,00)
        ventas.save()


        ventavideojuegos = VentaVideojuegos()
        ventavideojuegos.nombre_juego="free fire"
        ventavideojuegos.precio=3000000
        ventavideojuegos.save()

        ventaviajes = VentaViajes()
        ventaviajes.destino="San Andres"
        ventaviajes.valor_viaje= 50000000
        ventaviajes.descuento=True
        ventaviajes.save()


        regitrousuario = RegistroUsuario()
        regitrousuario.nombre_usuario="Cielo"
        regitrousuario.documento=123456789
        regitrousuario.save()

        usuarios = RegistroUs()
        usuarios.usuario=regitrousuario
        usuarios.correo="cielo1235@gmail.com"
        usuarios.save()
        

        fechacumpleannos=FechaCumpleannos()
        fechacumpleannos.nombre_completo="Celia Parra"
        fechacumpleannos.fecha= datetime.date(2022, 5, 20)
        fechacumpleannos.mensaje_cumple="feliz cumpleannos que la pase muy bien "
        fechacumpleannos.save()


        reservaciones =Reservaciones()
        reservaciones.nombres_completos="Carlos Perez"
        reservaciones.documento=123456974
        reservaciones.fecha_reservacion= datetime.date(2022, 5, 20)
        reservaciones.save()
        
        return HttpResponse('Esta es una prueba vista')


