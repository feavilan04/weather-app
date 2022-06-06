from dataclasses import field
from django.forms import ModelForm, TextInput
from .models import City 
from .models import Cordenada

class CityForm(ModelForm):
    class Meta:
        model = City 
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Nombre De La Ciudad'})}


