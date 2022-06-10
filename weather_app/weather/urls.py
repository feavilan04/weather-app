from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'home'),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
    path('sample-view', views.sample_view, name='sample_view')
]