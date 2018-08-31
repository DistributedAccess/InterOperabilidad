from dataclasses import dataclass

@dataclass
class Horario:
    Id_Bitacora:        str
    Id_Usuario:         str
    Hora_Entrada:       str
    Turno:              str
    Asistencia:         str
