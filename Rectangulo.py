class Rectangulo:
    def __init__(self, base, altura):
        self.base= base     
        self.altura=altura 

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
            return (self.base + self.altura)*2

    

base=int(input("Introdice la base del rectangulo: "))
altura=int(input("Introdice la altura del rectangulo: "))

rect1=Rectangulo(base,altura)

print(f"Área de rectangulo: {rect1.calcular_area()}")
print(f"Perimetro de rectangulo: {rect1.calcular_perimetro()}")