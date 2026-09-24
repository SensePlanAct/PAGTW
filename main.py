#!/usr/bin/env python
'''\
@Author: PAchi
@date: 17/09/2026
@email: sanchezbfrancisco@uniovi.es
'''

# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import bibloteca
import usuario
import libro

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    b=bibloteca.Bibloteca()
    u=usuario.Usuario()
    l=libro.Libro()
    print(b)
    print(u)
    print(l)

    l.agregarlibro("El Quijote DE LA MANCHA")
    l.agregarlibro("El Quijote DE LA MANCHA 2")
    l.agregarlibro("El Principito")
    l.agregarlibro("El Hobbit")

    u.agregarusuario("Carlota")
    u.agregarusuario("XUAN")
    u.agregarusuario("Rodrigo")
    u.agregarusuario("Pachi")

    print(b)
    print(u)
    print(l)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
