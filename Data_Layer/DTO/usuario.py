#from dataclasses import dataclass

#@dataclass
class Usuario:
    '''Id_Usuario:   str
    Nombre:       str
    Apellido_P:   str
    Apellido_M:   str
    Tipo_Usr:     str
    Activo:       str'''
    def __init__(self, Id_Usuario, Nombre, Apellido_P, Apellido_M, Tipo_Usr, Activo):
        self.Id_Usuario  =   Id_Usuario
        self.Nombre      =   Nombre
        self.Apellido_P  =   Apellido_P
        self.Apellido_M  =   Apellido_M
        self.Tipo_Usr    =   Tipo_Usr
        self.Activo      =   Activo
