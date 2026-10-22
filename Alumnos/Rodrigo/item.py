libros = []
revistas = []
digitales = []
prestados = []
class Item:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contador = 0
class Libro(Item):
    def __init__(self, nombre, paginas):
        super().__init__(nombre)
        self.paginas = paginas
        self.semanas = 2
        libros.append(self)
class Revista(Item):
    def __init__(self, nombre, paginas):
        super().__init__(nombre)
        self.paginas = paginas
        self.semanas = 1
        revistas.append(self)
class Digital(Item):
    def __init__(self, nombre, duracion):
        super().__init__(nombre)
        self.duracion = duracion
        self.semanas = 1
        digitales.append(self)
def prestar(item):
    prestados.append(item)
    item.contador += 1
    print(f"Se ha prestado: {item.nombre}")
def mostrar_prestados():
    for item in prestados:
        print(item.nombre)
libro1 = Libro("El Quijote", 450)
libro2 = Libro("Jeronimo Stilton", 500)
revista1 = Revista("Forbes", 100)
digital1 = Digital("Fightclub", 10)
prestar(libro1)
prestar(libro2)
prestar(revista1)
prestar(digital1)
print("\nPrestados:")
mostrar_prestados()