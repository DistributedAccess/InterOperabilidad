from Business_Api import *
import sys
sys.path.append("..")
from Infrastructure.Config import Config
from Infrastructure.Logging import Logging
from DTO.usuario import Usuario
from DTO.usuario import Horario
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
    def Registrar_Usuarios(json):
        Registrar_Usuarios_con_Horarios(json)


def Registrar_Usuarios_con_Horarios(users):

    for usr in users['Usuarios']:
        Registrar_Usuario(usr)


def Registrar_Usuario(usuario):

    usr = Usuario(usuario['Id_Usuario'],
                  usuario['Nombre'],
                  usuario['Apellido_M'],
                  usuario['Apellido_P'],
                  usuario['Tipo_Usuario'],
                  usuario['Activo'])

    Interop_CRUDS.Registrar(usr)
    Registrar_Horarios(usuario)

def Registrar_Horarios(usuario):

    for horario in usuario['Horario']
        Registrar_Horario(horario)

    for horario in usuario['Horario']
        usr_hor = Usuario_Horario(horario['Id_Horario']
                                  usuario['Id_Usuario'])
        Registrar_Usuario_Horario(usr_hor)


def Registrar_Horario(horario):
    hor = Horario(horario['Id_Horario'],
                  horario['Turno'],
                  horario['Inicio'],
                  horario['Fin'],
                  horario['Dia'])

    Interop_CRUDS.Registrar(hor)

def Registrar_Usuario_Horario(usr_h):
    usr_hor = Usuario_Horario(usr_h['Id_Horario'],
                              usr_h['Id_Usuario'])

    Interop_CRUDS.Registrar(usr_hor)
