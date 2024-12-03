from django import forms

# from django.forms.widgets import NumberInput

# class Formulario(forms.Form):
    # nombre = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    # email = forms.EmailField(label='Ponga un correo válido')
    # upload = forms.FileField(upload_to ='uploads/')

# class Formulario(forms.Form):
#     fecha_reservacion = forms.DateField(widget=NumberInput(attrs={'type':'date'}))

# class Formulario(forms.Form):
#     # platofavorito = forms.ChoiceField(choices=plato_favorito)
#     plato_favorito = [('italiana','italiana'),('griega','griega'),('india','india')]
#     platofavorito = forms.ChoiceField(widget=forms.RadioSelect, choices=plato_favorito)


##### Clase que enviará formulario a la BD
from .models import Logger

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'

