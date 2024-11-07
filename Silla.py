__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

from enum import enum
class silla:
    #Constructor
    def __init__ (self, Numero, Clase, ubicacion):
        self.__Numero = Numero
        self.__Clase = Clase
        self.__ubicacion = ubicacion
        self.__Pasajero = None

# Enmus

class Clase (enum):
    EJECUTIVA = "Ejecutiva"
    ECONOMICA = "Economica"

# metodos
def asignarPasajero (self):
    self.__Pasajero = None

def asignarSilla (self):
    self.__Pasajero = self.__Pasajero

def darNumero (self):
    return self.__Numero

def getClase (self):
    return self.__clase

def getUbicacion (self):
    return self.__Ubicacion

def getPasajero (self):
    return self.__Pasajero

