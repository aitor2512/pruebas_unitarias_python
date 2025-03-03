# Practica 2 - Biblioteca


import pytest
from biblioteca import Biblioteca , Libro

def test_libro_atributo():
    libro = Libro("1984", "George Orwell", 1949)
    assert libro.titulo == "1984"
    assert libro.autor == "George Orwell"
    assert libro.anio == 1949
    assert libro.prestado == False

def test_libro_prestado():
    biblioteca = Biblioteca()
    libro = Libro("1984", "George Orwell", 1949)
    biblioteca.agregar_libro(libro)
    assert str(libro) == "1984 de George Orwell (1949) - disponible"
    biblioteca.prestar_libro("1984")
    assert str(libro) == "1984 de George Orwell (1949) - prestado"

def test_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Seis de Cuervos", "Leigh Bardugo", 2015)
    biblioteca.agregar_libro(libro)
    assert len(biblioteca.libros) == 1
    assert biblioteca.libros[0].titulo == "Seis de Cuervos"

def test_eliminar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Seis de Cuervos", "Leigh Bardugo", 2015)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("Seis de Cuervos")
    assert len(biblioteca.libros) == 0

def test_prestar_libro_no_existente():
    """Verifica que intentar prestar un libro que no existe devuelva un mensaje adecuado"""
    biblioteca = Biblioteca()
    assert biblioteca.prestar_libro("Dune") == "El libro 'Dune' no se encuentra en la biblioteca."


def test_devolver_libro():
    """Verifica que un libro se devuelva correctamente"""
    biblioteca = Biblioteca()
    libro = Libro("Drácula", "Bram Stoker", 1897)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("Drácula")
    assert biblioteca.devolver_libro("Drácula") == "Has devuelto el libro 'Drácula'."
    assert libro.prestado == False


def test_devolver_libro_no_prestado():
    """Verifica que intentar devolver un libro que no estaba prestado devuelva un mensaje adecuado"""
    biblioteca = Biblioteca()
    libro = Libro("Drácula", "Bram Stoker", 1897)
    biblioteca.agregar_libro(libro)
    assert biblioteca.devolver_libro("Drácula") == "El libro 'Drácula' no estaba prestado."


def test_devolver_libro_no_existente():
    """Verifica que intentar devolver un libro que no existe devuelva un mensaje adecuado"""
    biblioteca = Biblioteca()
    assert biblioteca.devolver_libro("IT") == "El libro 'IT' no se encuentra en la biblioteca."
