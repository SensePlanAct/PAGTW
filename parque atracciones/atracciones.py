class Visitante:
    def __init__(self,dni, nombre:str, edad:int, altura:float) -> None:
        self.__dni = dni
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        lista=[]
    @property
    def dni(self):
        return self.__dni
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    def altura(self):
        return self.__altura
    def __str__(self):
        return f'Nombre: {self.nombre}\nDNI: {self.dni}\nEdad: {self.edad}\nAltura: {self.altura}\n'
    def mostrar_informacion(self):
        return(Visitante.__str__(self))


class Atraccion:
    def __init__(self, nombre: str, codigo, capacidad: int, altura_minima: float, abierta: str) -> None:
        self.__nombre = nombre
        self.__codigo = codigo
        self.__capacidad = capacidad
        self.__altura_minima = altura_minima
        self.__abierta = abierta
    @property
    def nombre(self):
        return self.__nombre
    @property
    def codigo(self):
        return self.__codigo
    @property
    def capacidad(self):
        return self.__capacidad
    @property
    def altura_minima(self):
        return self.__altura_minima
    @property
    def abierta(self):
        return self.__abierta
    def __str__(self):
        return f'Nombre: {self.nombre}\nCódigo: {self.codigo}\nCapacidad: {self.capacidad}\nAltura mímima: {self.altura_minima}\nAbierta o cerrrada: {self.abierta}\n'
    def mostrar_informacion(self):
        return(Atraccion.__str__(self))
    def abrir_atraccion(self):
        if self.__abierta == "ABIERTA":
            return f'La atracción ya esta abierta'
        else:
            self.__abierta = "ABIERTA"
            return f'Se ha abierto la atraccion'
    def cerrar_atraccion(self):
        if self.__abierta == "CERRADA":
            return f'La atracción ya esta cerrada'
        else:
            self.__abierta = "CERRADA"
            return f'Se ha cerrado la atraccion'
    def comprobar_persona(self,altura):
        if altura < self.altura_minima:
            return f'No puede usar la atracción'
        elif self.abierta == "CERRADA":
            return f'No puede usar la atracción'
        else:
            return f'Puede usar la atracción'

class MontanaRusa(Atraccion):
    def __init__(self,nombre: str, codigo: int, capacidad: int, altura_minima: float, abierta: str, velmax: float,edadmin:int) -> None:
        super().__init__(nombre, codigo, capacidad, altura_minima, abierta)
        self.__velmax = velmax
        self.__edadmin = edadmin
    @property
    def velmax(self):
        return self.__velmax
    @property
    def edadmin(self):
        return self.__edadmin
    def comprobar_persona(self,altura,edad):
        if super().comprobar_persona(altura) and edad >= self.edadmin:
            return f'Puede usar la atracción'
        else:
            return f'No puede usar la atracción'
    def __str__(self):
        return super().__str__()+f'\nVelocidad máxima: {self.velmax}\nEdad mínima: {self.edadmin}\n'

class AtraccionInfantil(Atraccion):
    def __init__(self,nombre: str, codigo: int, capacidad: int, altura_minima: float, abierta: str,edadmax:int) -> None:
        super().__init__(nombre, codigo, capacidad, altura_minima, abierta)
        self.__edadmax = edadmax
    @property
    def edadmax(self):
        return self.__edadmax
    def comprobar_persona(self, altura, edad):
        if super().comprobar_persona(altura) and edad <= self.edadmax:
            return f'Puede usar la atracción'
        else:
            return f'No puede usar la atracción'
    def __str__(self):
        return super().__str__()+f'\nEdad mínima: {self.edadmax}\n'



    """fichero=open("visitantes.txt")
    for linea in fichero:
        datos = linea.strip().split(";")
        dni = datos[0]
        nombre = str(datos[1])
        edad = int(datos[2])
        altura = float(datos[3])
    fichero.close()
    fichero = open("atracciones.txt")
    for linea in fichero:
        datos = linea.strip().split(";")
        tipo = int(datos[0])
        nombre = str(datos[1])
        codigo = (datos[2])
        capacidad = int(datos[3])
        if tipo == "MONTANA":
            altura_minima = float(datos[4])
            velmax = int(datos[5])
            edadmin = int(datos[6])
        else:
            altura_max = float(datos[4])
            edad_max = int(datos[5])
        abierta = str(datos[7])
    fichero.close()"""



p=Visitante(123,"yo",12,130)
print(p.mostrar_informacion())
print(p)
a=Atraccion("u",21,1231,130,"CERRADA")
print(a.mostrar_informacion())
print(a.abrir_atraccion())