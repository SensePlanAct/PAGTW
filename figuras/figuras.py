class Figuras:
    def __init__(self,tipo,base,altura):
        self.__base = base
        self.__altura = altura
        self.tipo=tipo


    def settipo(self,tipo):
        while tipo != "Triangulo" and tipo !="Cuadrado" and tipo !="Rectangulo":
            tipo=input(f'Introduce una figura valida')
        while tipo == "Cuadrado" and self.__base != self.__altura:
            print("La base y la altura deben ser iguales para un cuadrado")
            self.__base = float(input("Introduce la base: "))
            self.__altura = float(input("Introduce la altura: "))
        self.__tipo = tipo

    def __str__(self):
        return f"{self.__tipo,self.__base,self.__altura}"
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self,tipo):
        while tipo != "Triangulo" and tipo !="Cuadrado" and tipo !="Rectangulo":
            tipo=input(f'Introduce una figura valida')
        while tipo == "Cuadrado" and self.__base != self.__altura:
            print("La base y la altura deben ser iguales para un cuadrado")
            self.__base = float(input("Introduce la base: "))
            self.__altura = float(input("Introduce la altura: "))
        self.__tipo = tipo



f1=Figuras("Triangulo",10,20)
f2=Figuras("Cuadrado",3,20)
print(f1)
print(f2)
print(f1.tipo)
