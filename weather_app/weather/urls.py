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
    path('class-view', views.VistaPrueba.as_view(), name='class_view')
]