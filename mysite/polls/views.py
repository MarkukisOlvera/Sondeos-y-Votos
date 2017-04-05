from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, Estas en el indice del sitio.")
