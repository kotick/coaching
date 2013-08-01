# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
	user = models.OneToOneField(User,primary_key=True)
	total = models.CharField(max_length=30)

class Cliente(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	boletos = models.IntegerField(max_length=30)

class Clase(models.Model):
	id = models.AutoField('ID', primary_key=True)
	hangout = models.CharField(max_length=30)
	youtube = models.CharField(max_length=30)
	fecha = models.DateTimeField()
	estado = models.CharField(max_length=30)

	def __unicode__(self):
		return self.id

class Curso(models.Model):
	id = models.AutoField('ID', primary_key=True)
	nombre = models.CharField(max_length=30)
	profesor = models.ForeignKey(Profesor)
	vacantes = models.IntegerField(max_length=10)
	idioma = models.CharField(max_length=30)

class Curso_clase(models.Model):
	id = models.AutoField('ID', primary_key=True)
	curso = models.ForeignKey(Curso)
	clase = models.ForeignKey(Clase)

	def __unicode__(self):
		return self.id

class Cliente_curso(models.Model):
	id = models.AutoField('ID', primary_key=True)
	curso = models.ForeignKey(Curso)
	cliente = models.ForeignKey(Cliente)

	def __unicode__(self):
		return self.id