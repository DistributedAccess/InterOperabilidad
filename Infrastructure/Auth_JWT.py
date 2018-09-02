import datetime
import time
import json
import jwt
import sys
sys.path.append("..")
from Data_Layer.Interop_CRUDS import Interop_CRUDS
from Data_Layer.DTO.Usuario_Servidor import Usuario_Servidor

key = "88789061E1911A08A23E9BCE76238569383D6EE9C29BC3D712FC6E136AB0468A"

class Auth_JWT:

    @staticmethod
    def Crear_Token(usr, pas):
        token = jwt.encode(Payload(usr), key, algorithm='HS256')
        return token.decode(encoding="utf-8")

    @staticmethod
    def Expiracion(tkin):
        decoded = jwt.decode(tkin, key, algorithms='HS256')
        return datetime.datetime.fromtimestamp(decoded["exp"]).strftime('%c')

    #DEBE CONVERTIRSE EN UN DECORADOR
    @staticmethod
    def Validar_Token(tkin):
        def decovalidation(func):
            def wrapper():
                decoded = jwt.decode(tkin, key, algorithms='HS256')
                usr = decoded["iss"]
                consulta = Interop_CRUDS.Consultar_Uno(Usuario_Servidor(usr,''), 'User_Name', usr)

                if(len(consulta) != 0):
                    return func()
                else:
                    return False

            return wrapper
        return decovalidation

def Payload(usr):
    payload = {}
    payload['iss'] = usr
    payload['iat'] = int(time.time())
    payload['exp'] = int(time.time()+6000)
    return payload
