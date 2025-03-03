# Práctica 1 - Cine


import pytest
from cine import Pelicula

def test_compra_exitosa():
    pelicula = Pelicula("Ejemplo", 100, 8)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "Has comprado 5 entradas para Ejemplo. Total: $40"
    assert pelicula.asientos_disponibles == 95

def test_asientos_insuficientes():
    pelicula = Pelicula("Ejemplo2", 5, 10)
    resultado = pelicula.vender_entradas(10)
    assert resultado ==  "No hay suficientes asientos disponibles. Solo quedan 5 asientos."
    assert pelicula.asientos_disponibles == 5
def test_compra_cero_entradas():
    pelicula = Pelicula("Ejemplo3", 50, 9)
    resultado = pelicula.vender_entradas(0)
    assert resultado ==  "Error: La cantidad de entradas debe ser mayor a cero."
    assert pelicula.asientos_disponibles == 50