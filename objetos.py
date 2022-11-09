
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido= apellido

    def saludo(self):
        print("Hola, mi nombre es", self.nombre, self.apellido)


usuario= Usuario("mode","salgado")
usuario2= Usuario("nestor","salgado")
# print(usuario.nombre, usuario.apellido,usuario2.nombre, usuario2.apellido)
usuario.saludo()
usuario2.saludo()