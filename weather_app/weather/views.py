import datetime
from email import message
from multiprocessing import context
import random
import time
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .models import AnimalesZoologico, BirthdayRegistrationForm, Cantante, Celulares, City, Country, Department, DescripcionDeObjetosEncontrados, Estudiante, FechaCumpleannos, FullCity, InscripcionJuegosMesa, JuegosDeMesa, Jugador, Materias, Neighborhood, NewRegistrationForm, NombreDeporte, Genero, ObjetosEncontrados, PersonasViaje, Precios, President, Product, Registro, RegistroUs, RegistroUsuario, Reservaciones, VentaViajes, VentaVideojuegos, Ventas, RegistroFormulario, Location
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
    
    
class VistaPostFormulario(View):
    def get(self, request):
        
        return render(request, 'weather/vistapost.html')
    
    def post(self, request):
        primernombre= request.POST.get ('primer_nombre')
        segundonombre = request.POST.get('segundo_nombre')
        primerapellido = request.POST.get('primer_apellido')
        segundoapellido = request.POST.get('segundo_apellido')
        lista = request.POST.get('tipo_documento')
        numeroidentidad = request.POST.get('numero_Identidad')
        correoelectronico = request.POST.get('email')

        nuevo_registro=RegistroFormulario()
        nuevo_registro.primer_nombre=primernombre
        nuevo_registro.segundo_nombre=segundonombre
        nuevo_registro.primer_apellido=primerapellido
        nuevo_registro.segundo_apellido=segundoapellido
        nuevo_registro.document_type=lista
        nuevo_registro.numero_de_documento=numeroidentidad
        nuevo_registro.correo=correoelectronico
        nuevo_registro.save()
        
        
        dict = {
            'primer_nombre': primernombre,
            'segundo_nombre': segundonombre,
            'primer_apellido': primerapellido,
            'segundo_apellido': segundoapellido,
            'tipo_documento':lista,
            'numero_Identidad': numeroidentidad,
            'email': correoelectronico
        }
        
        
        print(request.POST.get ('primer_apellido'), flush=True)
        return render(request, 'weather/vistaformulario.html', dict )

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


class GetRecords(View):
    def get(self, request):
        allregistro=RegistroFormulario.objects.all()
        context={'allregistro':allregistro}
        return render(request,  'weather/vistafilas.html', context)

class BirthdayForm(View):
    def get(self, request):
        
        return render(request, 'weather/birthdayform.html')
    
    def post(self, request):
        firstname= request.POST.get ('first_name')
        secondname = request.POST.get('second_name')
        firstsurname = request.POST.get('first_surname')
        secondsurname = request.POST.get('second_surname')
        birthday =request.POST.get('birth_day')
        city = request.POST.get('city')
        language = request.POST.get('language')
        message = request.POST.get('message')

        new_message=BirthdayRegistrationForm()
        new_message.first_name=firstname
        new_message.second_name=secondname
        new_message.first_surname=firstsurname
        new_message.second_surname=secondsurname
        new_message.birth_day=birthday
        new_message.city=city
        new_message.language=language
        new_message.message=message
        new_message.save()
        
        
        dict = {
            'first_name': firstname,
            'secondname': secondname,
            'firstsurname': firstsurname,
            'secondsurname': secondsurname,
            'birth_day': birthday,
            'city': city,
            'language': language,
            'message':message
        }
        
        
        print(request.POST.get ('first_name'), flush=True)
        return redirect('list')


class BirthdayListing(View):
    def get(self, request):
        allregistration=BirthdayRegistrationForm.objects.all()
        context={'allregistration':allregistration}
        return render(request,  'weather/list.html', context)



class NewForm(View):
    def get(self, request):
        
        return render(request, 'weather/newform.html')

    def post(self, request):
        firstname= request.POST.get('first_name')
        secondname = request.POST.get('second_name')
        firstsurname = request.POST.get('first_surname')
        secondsurname = request.POST.get('second_surname')
        city = request.POST.get('city')

        names=NewRegistrationForm()
        names.first_name=firstname
        names.second_name=secondname
        names.first_surname=firstsurname
        names.second_surname=secondsurname
        names.city=city
        names.save()
        
        
        dict = {
            'first_name': firstname,
            'secondname': secondname,
            'firstsurname': firstsurname,
            'secondsurname': secondsurname,
            'city': city
            
        }
        
        
        print(request.POST.get ('first_name'), flush=True)
        return render(request, 'weather/newform.html', dict )

class Countries(View):
    def get(self, request):
        return render(request, 'weather/countries.html')

    def post(self, request):
        countryname= request.POST.get('country_name')
        telephoneindicative = request.POST.get('telephone_indicative')

        names=Country()
        names.country_name=countryname
        names.telephone_indicative=telephoneindicative
        names.save()
        
        dict = {
            'country_name': countryname,
            'telephone_indicative': telephoneindicative
            
        }
        print(request.POST.get ('country_name'), flush=True)
        return redirect('list_countries')
    
class CountriesListing(View):
    def get(self, request):
        allcities=Country.objects.all()
        context={'allcities':allcities}
        return render(request,  'weather/listcities.html', context)

class ProductForm(View):
    def get(self, request):
        countries=Country.objects.filter(id__gte =3)
        context={
            'countrieslist': countries
        }



        return render(request, 'weather/product.html', context)

    def post(self, request):
        country_id=request.POST.get('country')
        productname= request.POST.get('product_name')
        barcode = request.POST.get('barcode')
        technology = request.POST.get('technology')
        country_obj=Country.objects.get(id=country_id)
        
        
        products=Product()
        products.country=country_obj
        products.product_name=productname
        products.barcode=barcode
        products.technology=technology
        products.save()
        
        dict = {
            'country': country,
            'product_name': productname,
            'barcode': barcode,
            'technology': technology
        }
        print(request.POST.get ('country'), flush=True)
        return redirect('list_product')

class ProductListing(View):
    def get(self, request):
        allproduct=Product.objects.all()
        context={'allproduct':allproduct}
        return render(request,  'weather/listproduct.html', context)


class DepartmentForm(View):
    def get(self, request):
        countries=Country.objects.all()
        context={
            'countrieslist': countries
        }
        return render(request, 'weather/department.html', context)

    def post(self, request):
        country_id=request.POST.get('country')
        departmentname= request.POST.get('department_name')
        population = request.POST.get('population')
        country_obj=Country.objects.get(id=country_id)



        departments=Department()
        departments.country=country_obj
        departments.department_name=departmentname
        departments.population=population
        departments.save()
        
        
        print(request.POST.get ('department_name'), flush=True)
        return redirect('list_department')

class DepartmentListing(View):
    def get(self, request):
        department=Department.objects.all()
        context={'department':department}
        return render(request,  'weather/listdepartment.html', context)

class CitiesForm(View):
    def get(self, request):
        departments=Department.objects.all()
        context={
            'departmentlist': departments
        }
        return render(request, 'weather/city.html', context)

    def post(self, request):
        department_id=request.POST.get('department')
        city_name= request.POST.get('city_name')
        population = request.POST.get('population')
        airport = request.POST.get('airport')
        boolean_airport = True if airport == 'on' else False
        department_obj=Department.objects.get(id=department_id)
        
        
        city=FullCity()
        city.department=department_obj
        city.city_name=city_name
        city.population=population
        city.airport=boolean_airport
        city.save()
        
        print(request.POST.get ('department'), flush=True)
        return redirect('city_list')

class CityListing(View):
    def get(self, request):
        city=FullCity.objects.all()
        context={'city':city}
        return render(request,  'weather/listcity.html', context)

class LocationForm(View):
    def get(self, request):
        city=FullCity.objects.all()
        context={
            'citylist': city
        }
        return render(request, 'weather/location.html', context)

    def post(self, request):
        city_id=request.POST.get('city')
        location_name= request.POST.get('location_name')
        population = request.POST.get('population')
        city_obj=FullCity.objects.get(id=city_id)
        
        
        location=Location()
        location.city_location=city_obj
        location.location_name=location_name
        location.population=population
        location.save()
        
        print(request.POST.get ('city'), flush=True)
        return redirect('location_list')

class LocationListing(View):
    def get(self, request):
        location=Location.objects.all()
        context={'location':location}
        return render(request,  'weather/listlocation.html', context)


class NeighborhoodForm(View):
    def get(self, request):
        location=Location.objects.all()
        context={
            'locationlist': location
        }
        return render(request, 'weather/neighborhood.html', context)

    def post(self, request):
        location_id=request.POST.get('location')
        neighborhood_name= request.POST.get('neighborhood_name')
        population = request.POST.get('population')
        location_obj=Location.objects.get(id=location_id)

        neighborhood=Neighborhood()
        neighborhood.location_name=location_obj
        neighborhood.neighborhood_name=neighborhood_name
        neighborhood.population=population
        neighborhood.save()
        
        
        print(request.POST.get ('location'), flush=True)
        return redirect('neighborhood_list')

class NeighborhoodListing(View):
    def get(self, request):
        neighborhood=Neighborhood.objects.all()
        context={'neighborhood':neighborhood}
        return render(request,  'weather/listneighborhood.html', context)

class PresidentForm(View):
    def get(self, request):
        city=FullCity.objects.all()
        country=Country.objects.all()
        neighborhood=Neighborhood.objects.all()
        context={
            'citylist': city,
            'countrylist': country,
            'neighborhoodlist': neighborhood
        }
        return render(request, 'weather/president.html', context)

    def post(self, request):
        city_id=request.POST.get('city')
        country_id=request.POST.get('country')
        neighborhood_id=request.POST.get('neighborhood')
        name= request.POST.get('name')
        dateofbirth = request.POST.get('date_of_birth')
        city_obj=FullCity.objects.get(id=city_id)
        country_obj=Country.objects.get(id=country_id)
        neighborhood_obj=Neighborhood.objects.get(id=neighborhood_id)

        president=President()
        president.city_of_birth=city_obj
        president.country=country_obj
        president.neighborhood=neighborhood_obj
        president.name=name
        president.date_of_birth=dateofbirth
        president.save()
        
        
        print(request.POST.get ('city'), flush=True)
        return redirect('president_list')

class PresidentListing(View):
    def get(self, request):
        president=President.objects.all()
        context={'president':president}
        return render(request,  'weather/listpresident.html', context)

class UpdatePresident(View):
    def get(self, request, id_president):
        selected_president=President.objects.get(id=id_president)
        country=Country.objects.all()
        city=FullCity.objects.all()
        neighborhood=Neighborhood.objects.all()
        context={
            'selectedpresident': selected_president,
            'countrylist': country,
            'citylist': city,
            'neighborhoodlist': neighborhood
        }
        return render(request,  'weather/update_president.html', context)
    def post(self, request, id_president):
        selected_president=President.objects.get(id=id_president)
        country_id=request.POST.get('country')
        neighborhood_id=request.POST.get('neighborhood')
        name= request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        country_obj=Country.objects.get(id=country_id)
        neighborhood_obj=Neighborhood.objects.get(id=neighborhood_id)

        
        selected_president.name=name
        selected_president.country=country_obj
        selected_president.neighborhood=neighborhood_obj
        selected_president.date_of_birth=date_of_birth
        selected_president.save()
        
        
        print(request.POST.get ('country'), flush=True)
        return redirect('president_list')

class PresidentUpdateListing(View):
    def get(self, request):
        updatepresident=President.objects.all()
        context={'president':updatepresident}
        return render(request,  'weather/listpresident.html', context)

class UpdateFullCity(View):
    def get(self, request, id_city):
        selected_city=FullCity.objects.get(id=id_city)
        department=Department.objects.all()
        context={
            'selectedcity': selected_city,
            'departmentlist': department
        }
        return render(request,  'weather/update_city.html', context)
        
    def post(self, request, id_city):
        selected_city=FullCity.objects.get(id=id_city)
        department_id=request.POST.get('department')
        city_name=request.POST.get('city_name')
        population=request.POST.get('population')
        airport=request.POST.get('airport')
        department_obj=Department.objects.get(id=department_id)
        boolean_airport= True if airport == 'on' else False
        
        selected_city.department=department_obj
        selected_city.city_name=city_name
        selected_city.population=population
        selected_city.airport=boolean_airport
        selected_city.save()
              
        print(request.POST.get ('city_name'), flush=True)
        return redirect('city_list')

class FullCityUpdateListing(View):
    def get(self, request, ):
        updatecity=FullCity.objects.all()
        context={'city':updatecity}
        return render(request,  'weather/listcity.html', context)

class UpdateDepartment(View):
    def get(self, request, id_department):
        selected_department=Department.objects.get(id=id_department)
        country=Country.objects.all()
        context={
            'selecteddepartment': selected_department,
            'countrylist': country
        }
        return render(request,  'weather/update_department.html', context)
        
    def post(self, request, id_department):
        selected_department=Department.objects.get(id=id_department)
        country_id=request.POST.get('country')
        department_name=request.POST.get('department_name')
        population=request.POST.get('population')
        country_obj=Country.objects.get(id=country_id)
        
        selected_department.department_name=department_name
        selected_department.country_name=country_obj
        selected_department.population=population
        selected_department.save()
              
        print(request.POST.get ('country_name'), flush=True)
        return redirect('list_department')

class DepartmentUpdateListing(View):
    def get(self, request, ):
        updatedepartment=Department.objects.all()
        context={'department':updatedepartment}
        return render(request,  'weather/listdepartment.html', context)