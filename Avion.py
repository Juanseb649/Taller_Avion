__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

from Silla  import silla
from Silla import clase
from Silla import ubicacion
from Pasajero import Pasajero

class Avion:
    #constructor
    def __init__(self):
        self.numeroSillasEjecutivas = 8
        self.numeroSillasEconomicas = 42
        self.__sillaEjecutiva = []
        self.__sillaEconomica = []

        #sillas ejecutivas
        for i in range(self.numeroSillasEjecutivas):
            if i % 2 == 1:
                self.__sillaEjecutiva.append(silla(i + 1, clase.SillaEjecutiva, ubicacion.Pasillo))
            else:
                self.__sillaEjecutiva.append(silla(i + 1, clase.SillaEjecutiva, ubicacion.Ventana))

        #sillas economicas
        for i in range(self.numeroSillasEconomicas):
            if i % 3 == 1:
                self.__sillaEconomica.append(silla(i + 1, clase.Economica, ubicacion.Centro))
            elif i % 3 == 2:
                self.__sillaEconomica.append(silla(i + 1, clase.Economica, ubicacion.Pasillo))
            else:
                self.__sillaEconomica.append(silla(i + 1, clase.Economica, ubicacion.Ventana))

    #metodos
    def asignarSilla(self, silla, pasajero, clase, ubicacion, nombre: str, cedula: int) -> silla:
        #valores
        if clase != clase.Ejecutiva and clase != clase.Economica:
            raise Exception("Clase no reconocida")
        if ubicacion != ubicacion.Centro and ubicacion != ubicacion.Pasillo and ubicacion != ubicacion.Ventana:
            raise Exception("Ubicación no reconocida")
        if cedula == 0 or cedula is None:
            raise Exception("Cedula no reconocida")

        #Pasajero
        pasajero = Pasajero(cedula, nombre)

        #Asignar silla ejecutiva
        if clase == clase.Ejecutiva:
            for silla in self.__sillaEjecutiva:
                if not silla.sillaAsignada() and silla.darUbicacion() == ubicacion:
                    silla.asignarPasajero(pasajero)
                    return silla
            raise Exception("No hay sillas de la clase ejecutiva")

        #Asignar silla economica
        elif clase == clase.Economica:
            for silla in self.__sillaEconomica:
                if not silla.sillaAsignada() and silla.darUbicacion() == ubicacion:
                    silla.asignarPasajero(pasajero)
                    return silla
            raise Exception("No hay sillas de la clase economica")
        
        #Manejar error
        else:
            raise Exception("Error en la asignacion de la silla")

    def buscarPasajero(self, cedula: int) -> silla:
        #Validar valores
        if cedula == 0 or cedula is None:
            raise Exception("Cedula no reconocida")

        #Buscar en sillas ejecutivas
        for silla in self.__sillaEjecutiva:
            if silla.sillaAsignada() and silla.darPasajero().darCedula() == cedula:
                return silla

        #Buscar en sillas economicas
        for silla in self.__sillaEconomica:
            if silla.sillaAsignada() and silla.darPasajero().darCedula() == cedula:
                return silla

        #Manejar error
        raise Exception("No se encontro al pasajero")
    
    def eliminarReserva(self, cedula: int) -> None:
        #Validar valores
        if cedula == 0 or cedula is None:
            raise Exception("Cedula no reconocida")

        #Buscar pasajero
        try:
            silla = self.buscarPasajero(cedula)
            silla.desAsignarPasajero()
            
            #Eliminar silla
            if silla.darClase() == clase.Ejecutiva:
                self.__sillaEjecutiva.remove(silla)
            elif silla.darClase() == clase.Economica:
                self.__sillaEconomica.remove(silla)
        except Exception:
            raise Exception("No se encontro al pasajero")

    def calcularPorcentajeOcupacion(self) -> float:
        totalSillasOcupadas = 0
        
        for silla in self.__sillaEjecutiva:
            if silla.sillaAsignada():
                totalSillasOcupadas += 1
                
        for silla in self.__sillaEconomica:
            if silla.sillaAsignada():
                totalSillasOcupadas += 1
                
        totalSillas = self.numeroSillasEjecutivas + self.numeroSillasEconomicas
        return (totalSillasOcupadas / totalSillas) * 100