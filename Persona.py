""" Encapsulamiento de todos los atributos de una clase """

class Persona:
    def __init__(self,nombre, apellido, edad, *valores, **terminos) :
        self._nombre=nombre
        self._apellido=apellido
        self._edad= edad
        self._valores= valores
        self._terminos=terminos

    # permiso de lectura get
    @property
    def nombre(self):
        return self._nombre

    #llamando a m'etodo set nombre
    @nombre.setter
    def nombre(self,nombre):
        
        self._nombre=nombre


    # permiso de lectura get
    @property
    def apellido(self):
        return self._apellido

    #llamando a m'etodo set apellido
    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido

    # permiso de lectura get
    @property
    def edad(self):
        return self._edad

    #llamando a m'etodo set apellido
    @edad.setter
    def edad(self,edad):
        self._edad=edad