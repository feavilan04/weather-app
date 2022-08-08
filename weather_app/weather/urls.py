from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'home'),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
    path('prueba-view', views.Prueba.as_view(), name='prueba_view'),
    path('index-view',views.IndexPrueba.as_view(), name='index_view'),
    path('pagina2-view', views.VistaDos.as_view(), name='pagina2_view'),
    path('pagina3-view', views.VistaTres.as_view(), name='pagina3_view'),
    path('pagina4-view', views.VistaCuatro.as_view(), name='pagina4_view'),
    path('pagina5-view', views.VistaCinco.as_view(), name='pagina5_view'),
    path('sample-view', views.SampleView.as_view(), name='sample_view'),
    path('class-view', views.VistaPrueba.as_view(), name='class_view'),
    path('post-view',views.VistaPostFormulario.as_view(), name='post_view'),
    path('prueba-relaciones', views.InsercionModelos.as_view(), name='prueba_relaciones'),
    path('filas', views.GetRecords.as_view(), name='filas'),
    path('birthday-form', views.BirthdayForm.as_view(), name='birthday_form'),
    path('list', views.BirthdayListing.as_view(), name='list'),
    path('countries', views.Countries.as_view(), name='countries'),
    path('list-countries',views.CountriesListing.as_view(), name='list_countries'),
    path('product', views.ProductForm.as_view(), name='product'),
    path('list-product',views.ProductListing.as_view(), name='list_product'),
    path('department', views.DepartmentForm.as_view(), name='department'),
    path('list-department',views.DepartmentListing.as_view(), name='list_department'),
    path('city', views.CitiesForm.as_view(), name='city'),
    path('city-list', views.CityListing.as_view(), name='city_list'),
    path('location', views.LocationForm.as_view(), name='location'),
    path('location-list', views.LocationListing.as_view(), name='location_list'),
    path('neighborhood', views.NeighborhoodForm.as_view(), name='neighborhood'),
    path('neighborhood-list', views.NeighborhoodListing.as_view(), name='neighborhood_list')
]