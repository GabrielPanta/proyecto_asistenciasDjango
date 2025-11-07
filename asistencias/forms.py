from django import forms
from .models import Empresa

class LoginForm(forms.Form):
    empresa = forms.ChoiceField(choices=Empresa.choices, widget=forms.Select())
    password = forms.CharField(widget=forms.PasswordInput)

class UploadFileForm(forms.Form):
    mes = forms.ChoiceField(choices=[
        ("Enero","Enero"),("Febrero","Febrero"),("Marzo","Marzo"),("Abril","Abril"),
        ("Mayo","Mayo"),("Junio","Junio"),("Julio","Julio"),("Agosto","Agosto"),
        ("Septiembre","Septiembre"),("Octubre","Octubre"),("Noviembre","Noviembre"),("Diciembre","Diciembre")
    ])
    archivo = forms.FileField()

class ConsultaForm(forms.Form):
    empresa = forms.ChoiceField(choices=Empresa.choices)
    dni = forms.CharField(label="DNI")
    mes = forms.ChoiceField(choices=[
        ("Enero","Enero"),("Febrero","Febrero"),("Marzo","Marzo"),("Abril","Abril"),
        ("Mayo","Mayo"),("Junio","Junio"),("Julio","Julio"),("Agosto","Agosto"),
        ("Septiembre","Septiembre"),("Octubre","Octubre"),("Noviembre","Noviembre"),("Diciembre","Diciembre")
    ])
