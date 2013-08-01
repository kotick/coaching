# -*- encoding: utf-8 -*-
 
##
# App: app
##
 
 # Core
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
 
# Forms
from forms import *
 
# Decorators
from django.contrib.auth.decorators import login_required
 
# Messages, Login, Logout and User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
 
# Models
from Clases.models import *
 
# JSON
from django.utils import simplejson
from django.utils.safestring import SafeString
 
# Data Structures
from django.utils.datastructures import SortedDict
 
def index(request):
    
    title = 'Coaching Poliglota'
    login_form = LoginForm()
    regis_form = RegisForm()
    cursos = Curso.objects.all()
    return render_to_response(
        'Clases/index.html',
        {
            'title': title,
            'login_form': login_form,
            'cursos':cursos,
            'regis_form': regis_form
        },
        context_instance=RequestContext(request)
    )
    
def quienessomos(request):
    
    title = 'Quienes Somos'
    login_form = LoginForm()
    return render_to_response(
        
        'Clases/quienessomos.html',
        {
            'title': title,
            'login_form': login_form
        },
        context_instance=RequestContext(request)
    )

def profesor(request):
    if not request.user.profesor:        
        return HttpResponseRedirect('/')
    title = 'Profesor'
    login_form = LoginForm()

    return render_to_response(
        'Clases/profesor.html',
        {
            'title': title,
            'login_form': login_form
        },
        context_instance=RequestContext(request)
    )

def comofunciona(request):
    
    title = 'Como Funciona'
    login_form = LoginForm()

    return render_to_response(
        
        'Clases/comofunciona.html',
        {
            'title': title,
            'login_form': login_form
        },
        context_instance=RequestContext(request)
    )
def inscribete(request):
    
    title = 'Inscribete'
    login_form = LoginForm()

    return render_to_response(
        
        'Clases/inscribete.html',
        {
            'title': title,
            'login_form': login_form
        },
        context_instance=RequestContext(request)
    )
def login_view(request):
    """
    Vista encargada autenticar un usuario para ingresar al sistema
    """
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # redireccionar al inicio
                return HttpResponseRedirect('/')
            else:
                # warning
                #messages.warning(request, 'Tu cuenta ha sido desactivada.')
                #return HttpResponseRedirect('/')
                return HttpResponse('<h1>ERROR desactivada</h1>')
        else:
            # error
            #messages.error(request, 'Nombre de usuario o contraseña errónea.')
            #return HttpResponseRedirect('/')
            return HttpResponse('<h1>ERROR no existe</h1>')
    else:
        return HttpResponseRedirect('/')

def crear_usuario(request):

    if not request.user.is_anonymous():
        return HttpResponse('<h1>ERROR no es anonimo</h1>')

    if not request.method == 'POST':
        return HttpResponse('<h1>ERROR no es post</h1>')

    form = RegisForm(request.POST)
    
    # El formulario debe ser válido
    if not form.is_valid():
        return HttpResponse('<h1>Formulario Malo</h1>')
    # ----- Valido

    name = request.POST['username']
    pass1 = request.POST['password1']
    pass2 = request.POST['password2']

    if pass1 != pass2:
        return HttpResponse('<h1>Las password no son iguales</h1>')

    new_user = User(username=name)
    new_user.set_password(pass1)
    new_user.save()
    new_profesor = Profesor(user=new_user)
    new_profesor.save()
    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')