import sys
sys.path.append("../..")
from Data_Layer.Interop_CRUDS import Interop_CRUDS
from Infrastructure.Config import Config
from Infrastructure.Logging import Logging
from Data_Layer.DTO.usuario import Usuario
from Data_Layer.DTO.Horario import Horario
from Data_Layer.DTO.Usuario_Horario import Usuario_Horario
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
        return("OK")

def Respuesta():
    pass

def Registrar_Usuarios_con_Horarios(users):

    for usr in users['Usuarios']:
        Registrar_Usuario(usr)


def Registrar_Usuario(usuario):

    usr = Usuario(usuario['Usuario']['Id_Usuario'],
                  usuario['Usuario']['Nombre'],
                  usuario['Usuario']['Apellido_P'],
                  usuario['Usuario']['Apellido_M'],
                  usuario['Usuario']['Tipo_Usuario'],
                  usuario['Usuario']['Activo'])

    Interop_CRUDS.Registrar(usr)
    Registrar_Horarios(usuario)

def Registrar_Horarios(usuario):

    for horario in usuario['Horario']:
        Registrar_Horario(horario)

    for horario in usuario['Horario']:
        usr_hor = Usuario_Horario(horario['Id_Horario'],
                                  usuario['Usuario']['Id_Usuario'])
        Registrar_Usuario_Horario(usr_hor)


def Registrar_Horario(horario):
    hor = Horario(horario['Id_Horario'],
                  horario['Turno'],
                  horario['Inicio'],
                  horario['Fin'],
                  horario['Dia'])

    Interop_CRUDS.Registrar(hor)

def Registrar_Usuario_Horario(usr_h):
    Interop_CRUDS.Registrar(usr_h)
