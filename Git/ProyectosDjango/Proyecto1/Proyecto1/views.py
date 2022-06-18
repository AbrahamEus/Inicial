from contextvars import Context
from datetime import datetime
from multiprocessing import context
from pipes import Template
from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido 
    
def saludo(request):#primera vista
   p1=Persona("Juan","Marcelo")
   temas =["Pla ntillas","Modelos","Formularios","Vistas","Despliegue"]
   #nombre="Juan"
   #apellido="Diaz"
   fecha_actual= datetime.now()
   #doc_externo = open(C:/Users/abram/Desktop/Curso 1/ProyectosDjango/Proyecto1/Proyecto1/Plantillas/index.html")#carga documentos externo
   #plt= Template(doc_externo.read())
   #doc_externo.close()
   #doc_externo = loader.get_template('index.html')
   
   #ctx= Context()
   #documento = doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"Hora_actual":fecha_actual, "temas":temas})

   return render(request,"index.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"Hora_actual":fecha_actual, "temas":temas})

def adios(request):


    return HttpResponse("Adios")

def dameFecha(request):
    fecha_actual= datetime.strftime()
    doc = """<html>
   <body>
   <h1>
   Fecha y hora actuales %s
   </h1>
   </body>
   <html>""" % fecha_actual
    return HttpResponse(doc)

def calculaEdad(request,edad, agno):
    
    periodo= agno-2022
    edadFutura= edad+periodo
    documento="""
    <html>
    <body>
    <h2>
    En el año %s tendras %s años
    </h2>
    </body>
    </html> 
    """%(agno,edadFutura)
    return HttpResponse(documento)