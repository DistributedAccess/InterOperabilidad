import sys
sys.path.append("../..")
from Data_Layer.DTO.Usuario_Servidor import Usuario_Servidor
from Data_Layer.Interop_CRUDS import Interop_CRUDS
from Infrastructure.Auth_JWT import Auth_JWT
from Infrastructure.Logging import Logging
import datetime

import hashlib
import json
import jwt

logg    = Logging()

class Interop_Login:
    @staticmethod
    def Interop_Login(jsn):
        valid =  Validar(jsn)
        if(valid == None):
            usr = jsn['u']
            pas = jsn['p']
            if(Autenticar(usr,pas)):
                tkn = Generar_Token(usr,pas)
                return Respuesta(tkn[0], str(tkn[1]))
            else:
                data = {}
                data['CodigoError'] = 401
                data['MensajeError'] = "El usuario o la contrasena no coinciden"
                data['timeStamp'] = str(datetime.datetime.now())
                return json.dumps(data)
        else:
            return valid

def Validar(jsn):
    data = {}
    if 'u' not in jsn:
        data['CodigoError'] = 400
        data['MensajeError'] = "Formato json no valido"
        data['timeStamp'] = str(datetime.datetime.now())
        return json.dumps(data)
    if 'p' not in jsn:
        data['CodigoError'] = 400
        data['MensajeError'] = "Formato json no valido"
        data['timeStamp'] = str(datetime.datetime.now())
        return json.dumps(data)
    if (jsn['u'] == '' or jsn['p'] == ''):
        data['CodigoError'] = 400
        data['MensajeError'] = "Falta un parametro de entrada"
        data['timeStamp'] = str(datetime.datetime.now())
        return json.dumps(data)


def Autenticar(usr, pas):
    """     Consulta el usuario en la base de datos, en caso de existir hashea el
        pas y lo compara con la consulta en caso de ser igual retornara un true.
        def Autenticar(usr, pas):
    """
    logg.debug("Se procede a comparar en base...")
    flag = True

    hash  = hashlib.sha256(str.encode(pas))
    consulta = Interop_CRUDS.Consultar_Uno(Usuario_Servidor(usr,pas), 'User_Name', usr)
    if(len(consulta) != 0):
        if(hash.hexdigest() == consulta[0][2].lower()):
            logg.info("Credenciales autenticadas!!!")
            flag = True
        else:
            logg.info("Usuario no autenticado!")
            flag = False
    else:
        logg.info("No hay usuarios en la base o hay un error en la base")
        flag = False

    return flag

def Generar_Token(usr, pas):
    token = Auth_JWT.Crear_Token(usr, pas)
    time  = Auth_JWT.Expiracion(token)
    logg.info("Se ha generado un token al usuario: " + usr)
    return  token, time


def Respuesta(token, timestamp):
    """     Genera un json que contiene el token y el timestamp """

    data = {}
    data['jwtToken'] = token
    data['passwordExpiration'] = timestamp

    return json.dumps(data)
