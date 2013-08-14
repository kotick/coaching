# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
	user = models.OneToOneField(User,primary_key=True)

class Cliente(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	boletos = models.IntegerField(max_length=30)

class Administrador(models.Model):
	user = models.OneToOneField(User, primary_key=True)

class Curso(models.Model):
	nombre = models.CharField(max_length=30)
	profesor = models.ForeignKey(Profesor)
	vacantes = models.IntegerField(max_length=10)
	idioma = models.CharField(max_length=30)
	miembros = models.IntegerField(max_length=10)
	cantidad_clases = models.IntegerField(max_length=10)
	dia_inicio = models.CharField(max_length=30)
	estado =models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre

class Clase(models.Model):
	curso = models.ForeignKey(Curso)
	nombre  = models.CharField(max_length=30)
	dia = models.CharField(max_length=30)
	hora = models.CharField(max_length=30)
	hangout = models.CharField(max_length=30)
	youtube = models.CharField(max_length=30)
	estado = models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre

class curso_cliente(models.Model):
	curso = models.ForeignKey(Curso)
	cliente = models.ForeignKey(Cliente)