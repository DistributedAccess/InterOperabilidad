from Business_Api import *
import sys
sys.path.append("..")
from Infrastructure.Config import Config
from Infrastructure.Logging import Logging
from DTO.usuario import Usuario
import json

class Interop_Registrar:
"""     Esta clase es la encargada de hacer todo la logica de negocio
        de la api: /Interoperabilidad/Registro, la cual recibira un
        objeto Json el cual contendra a los usuarios con sus respectivos
        horarios.

        Esta clase ingresa a la base de datos los objetos recibidos,
        descomprime y entrena al controlador con las imagenes de los usuarios
        descomprimidas
"""


    @staticmethod
    def DoSomething():
        pass

def Registrar_Usuarios(users):

    for usr in users['Usuarios']:
        Registrar_Usuario(usr)

def Registrar_Usuario(usuario):

    #usr = Usuario("2010020726","Alice","Vargas","Echeverria","Administrador","True")
    usr = Usuario(usuario['Id_Usuario'],
                  usuario['Nombre'],
                  usuario['Apellido_M'],
                  usuario['Apellido_P'],
                  usuario['Tipo_Usuario'],
                  usuario['Activo'])

    Interop_CRUDS.Registrar(usr)

    for horario in usuario['Horario']
        Registrar_Horario(horario)


def Registrar_Horario(horario):
    pass
