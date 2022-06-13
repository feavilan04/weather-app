from multiprocessing import context
import random
import time
from tkinter.font import names
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .models import City
from .forms import CityForm
import random
# Create your views here.
def index_prueba(request):
    name = [
        'juan',
        'carlos',
        'pepe',
        'jose']
    name = names[random.randint(0, len(names) - 1)]
    context = {
        'nombre_seleccionado':name
    }
    return render(request, 'weather/vista1.html',context)
    

def pagina2(request):
	return render(request, 'weather/vista2.html', {})


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

def prueba(request):
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

def sample_view(request):
    # create list with 20 names and return a random one
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
    
    
