from django import forms 
from .models import Movie
from django.forms.widgets import NumberInput, DateInput
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'release_date' : forms.DateInput(attrs={'type':'date'}),
            'score' : forms.NumberInput(attrs={'min':0,'max':5,'step':0.5})
        }