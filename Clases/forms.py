# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.admin import widgets
from Clases.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}),label= 'Usuario')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label= 'Contraseña')

class RegisForm(forms.Form):
	username =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}),label= 'Usuario')
	password1 =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label= 'Contraseña')
	password2 =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),label= 'Nuevamente la contraseña')

class CrearCurso(forms.Form):
	nombre = forms.CharField(label='Nombre del curso :',max_length='30')
	vacantes = forms.CharField(label='Numero de vacantes :',max_length='30')
	idioma = forms.CharField(label='Idioma a enseñar :',max_length='30')
	inicio = forms.CharField(label='Fecha de inicio:',max_length='30')

class IniciarClase(forms.Form):
	Youtube = forms.CharField(label='Ingrese la dirección de Youtube :',max_length=200)
	Hangout = forms.CharField(label='Ingrese la dirección de Hangout :',max_length=200)

class Profesor(forms.Form):
	nombre = forms.CharField(label='Nombre del profesor :',max_length=30)
	aprellido = forms.CharField(label='Apellido del profesor :',max_length=30)
	usuario = forms.CharField(label='Nombre de usuario del profesor:',max_length=30)

class Cliente(forms.Form):
	nombre =forms.CharField(label='Nombre :',max_length=30)
	apellido =forms.CharField(label='Apellido :',max_length=30)

class CrearClase(forms.Form):
	SeleccionCurso =forms.ModelChoiceField(queryset=Curso.objects.all(),widget=forms.Select(), label='Selecciona un condominio')
	nombre =forms.CharField(max_length=100,label= 'Nombre de la clase')
	dia =forms.CharField(max_length=100,label= 'fecha de la clase')
	hora =forms.CharField(max_length=100,label= 'hora de la clase')
