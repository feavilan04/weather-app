from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'home'),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
    path('prueba', views.prueba, name='prueba'),
    path('index-prueba',views.index_prueba, name='index_prueba'),
    path('pagina-prueba', views.pagina2, name='pagina_prueba'),
]