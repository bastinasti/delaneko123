from django.urls import path
from .views import inicio, registro, seccionperro, secciongato, seccionexotico, iniciosesion, plantillaProducts, simple_checkout, carrito, micarrito, registrarusuario

urlpatterns =[
    path('',inicio, name="inicio"),
    path('registro/', registro, name="registro"),
    path('registrarusuario', registrarusuario, name="registrar"),
    path('seccionperro/',seccionperro, name="seccionperro"),
    path('secciongato/',secciongato, name="secciongato"),
    path('seccionexotico/',seccionexotico, name="seccionexotico"),
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('plantillaProducts/<idProducto>', plantillaProducts, name="plantillaProducts"),
    path('<slug>/carrito', carrito, name="carrito"),
    path('micarrito/', micarrito, name="micarrito"),




]