'''\
@Author: PAchi
@date: 17/09/2026
@email: sanchezbfrancisco@uniovi.es
'''

class Usuario:

    usuarios = []

    def __init__(self):
        self.usuarios = []
        self.contadorU = 0

    def __str__(self):
        print(self.usuarios)
        return f"Esta es la clase Usuario con {self.contadorU} usuarios"

    def agregarusuario(self, item):
        self.usuarios.append(item)
        self.contadorU += 1
