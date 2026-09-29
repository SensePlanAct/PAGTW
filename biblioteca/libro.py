'''\
@Author: PAchi
@date: 17/09/2026
@email: sanchezbfrancisco@uniovi.es
'''
from typing import override


class Libro:

    libros = []
    def __init__(self):
        self.libros= []
        self.contadorL = 0

    @override
    def __str__(self):
        print(self.libros)
        return f"Esta es la clase Bibloteca con {self.contadorL} libros"

    def agregarlibro(self, libro):
        self.libros.append(libro)
        self.contadorL += 1
