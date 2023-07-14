from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.
# /productos


def index(request):
    productos = Producto.objects.all().values()
    # print(productos)
    # return HttpResponse('Hola Mundo!')
    # return HttpResponse(producto[0].nombre)
    return JsonResponse(list(productos), safe=False)
    # producto = Producto.objects.filter(puntaje=3)
    # producto = Producto.objects.get(id=3)
