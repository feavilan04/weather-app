from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'home'),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
    path('prueba', views.prueba, name='prueba'),
    path('index-prueba',views.index_prueba, name='index_prueba'),
    path('pagina-prueba', views.pagina2, name='pagina_prueba'),
    path('pagina-prueba3', views.pagina3, name='pagina_prueba3'),
    path('pagina-prueba4', views.pagina4, name='pagina_prueba4'),
    path('pagina-prueba5', views.pagina5, name='pagina_prueba5'),
]