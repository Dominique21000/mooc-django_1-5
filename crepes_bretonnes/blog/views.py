#-*- coding: utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
import os 
# Create your views here.

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <title>Bienvenue sur mon blog</title>
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)

def tpl(request):
    maPath = os.path.abspath(__file__)
    return render(request, 'blog/tpl.html',{'current_date':datetime.now(),'maPath':maPath})

def addition(request, nombre1, nombre2):
    totalSomme = int(nombre1) + int(nombre2)
    totalMultiplication= int(nombre1) * int(nombre2)
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())
