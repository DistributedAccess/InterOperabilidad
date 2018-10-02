from Business_Layer.Business_Api.Interop_ZipRegistrar import Interop_ZipRegistrar
import sys
sys.path.append("../..")
from Data_Layer.Interop_CRUDS import Interop_CRUDS
from Infrastructure.Config import Config
from Infrastructure.Logging import Logging
from Data_Layer.DTO.usuario import Usuario
from Data_Layer.DTO.Horario import Horario
from Data_Layer.DTO.Usuario_Horario import Usuario_Horario
import json
import datetime

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

        #   Se valida y se descomprime el zip
        lstOks = Interop_ZipRegistrar.ZipRegistrar(json)

        #   Se registra en Base de Datos
        Registrar_Usuarios_con_Horarios(json)

        #   Se genera y se retorna una Respuesta
        return Respuesta(lstOks)

def Respuesta(lstOks):

    data = {}
    data['timeStamp'] = str(datetime.datetime.now())

    user = []

    for usr in lstOks:
        user.append(Respuesta_Usr(usr))

    data['trackingIds'] = user

    data['Mensaje'] = str(datetime.datetime.now())
    return json.dumps(data)

def Respuesta_Usr(usr):

    user = {}

    if(usr[1] == True):
        user['Usuario'] = usr[0]
        user['CodigoError'] = "201"
        user['Mensaje'] = "Usuario Registrado"
    else:
        user['Usuario'] = usr[0]
        user['CodigoError'] = "404"
        user['Mensaje'] = "No se registro al usuario"

    return user

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
