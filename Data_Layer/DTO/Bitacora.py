#from dataclasses import dataclass

#@dataclass
class Horario:
    ''' Id_Bitacora:        str
    Id_Usuario:         str
    Hora_Entrada:       str
    Turno:              str
    Asistencia:         str '''

    def __init__(self, Id_Bitacora,Id_Usuario,Hora_Entrada,Turno,Asistencia):
        self.Id_Bitacora  = Id_Bitacora
        self.Id_Usuario   = Id_Usuario
        self.Hora_Entrada = Hora_Entrada
        self.Turno        = Turno
        self.Asistencia   = Asistencia
