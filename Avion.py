__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

from Silla import silla
from Silla import clase
from Silla import ubicacion
from Pasajero import Pasajero

class Avion:
    # Constructor
    def __init__(self):
        self.numeroSillasEjecutivas = 8
        self.numeroSillasEconomicas = 42
        self.__sillaEjecutiva = []
        self.__sillaEconomica = []

        # Sillas ejecutivas
        for i in range(self.numeroSillasEjecutivas):
            if i % 2 == 1:
                self.__sillaEjecutiva.append(silla(i + 1, clase.SillaEjecutiva, ubicacion.Pasillo))
            else:
                self.__sillaEjecutiva.append(silla(i + 1, clase.SillaEjecutiva, ubicacion.Ventana))

        # Sillas económicas
        for i in range(self.numeroSillasEconomicas):
            if i % 3 == 1:
                self.__sillaEconomica.append(silla(i + 1, clase.Economica, ubicacion.Centro))
            elif i % 3 == 2:
                self.__sillaEconomica.append(silla(i + 1, clase.Economica, ubicacion.Pasillo))
            else:
                self.__sillaEconomica.append(silla(i + 1, clase.Economica, ubicacion.Ventana))

    # Métodos

    def asignarSilla(self, silla, pasajero, clase, ubicacion, nombre: str, cedula: int) -> silla:
        # Validación de valores
        if clase != clase.Ejecutiva and clase != clase.Economica:
            raise Exception("Clase no reconocida")
        if ubicacion != ubicacion.Centro and ubicacion != ubicacion.Pasillo and ubicacion != ubicacion.Ventana:
            raise Exception("Ubicación no reconocida")
        if cedula == 0 or cedula is None:
            raise Exception("Cedula no reconocida")

        # Crear pasajero
        pasajero = Pasajero(cedula, nombre)

        # Asignar silla ejecutiva
        if clase == clase.Ejecutiva:
            for silla in self.__sillaEjecutiva:
                if not silla.sillaAsignada() and silla.darUbicacion() == ubicacion:
                    silla.asignarPasajero(pasajero)
                    return silla
            raise Exception("No hay sillas de la clase ejecutiva")

        # Asignar silla económica
        elif clase == clase.Economica:
            for silla in self.__sillaEconomica:
                if not silla.sillaAsignada() and silla.darUbicacion() == ubicacion:
                    silla.asignarPasajero(pasajero)
                    return silla
            raise Exception("No hay sillas de la clase económica")
        
        raise Exception("Error en la asignación de la silla")

    def buscarPasajero(self, cedula: int) -> silla:
        # Validar valores
        if cedula == 0 or cedula is None:
            raise Exception("Cedula no reconocida")

        # Buscar en sillas ejecutivas
        for silla in self.__sillaEjecutiva:
            if silla.sillaAsignada() and silla.darPasajero().darCedula() == cedula:
                return silla

        # Buscar en sillas económicas
        for silla in self.__sillaEconomica:
            if silla.sillaAsignada() and silla.darPasajero().darCedula() == cedula:
                return silla