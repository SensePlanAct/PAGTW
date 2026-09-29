'''\
@Author: PAchi
@date: 17/09/2026
@email: sanchezbfrancisco@uniovi.es
'''

class Bibloteca:

    nombre = "Bernaldo de Quirós"
    bibliotecaria = "Magadalena"
    usuarios = []
    libros = []
    def __init__(self):
        self.usuarios = []
        self.libros= []
        self.contadorU = 0
        self.contadorL = 0

    def __str__(self):
        usuarios = 343
        print(self.libros)
        print(self.usuarios)
        return f"Esta es la clase Bibloteca con {self.contadorL} libros y {self.contadorU} usuarios"

    def agregarusuario(self, item):
        self.usuarios.append(item)
        self.contadorU += 1

    def agregarlibro(self, libro):
        self.libros.append(libro)
        self.contadorL += 1
