import sys
sys.path.append("../..")
from Infrastructure.Config import Config
from Infrastructure.Logging import Logging
from Data_Layer.DTO.Usuario_Servidor import Usuario_Servidor
from Data_Layer.Interop_CRUDS import Interop_CRUDS

import hashlib
import json
import jwt

class Interop_Login:

    def Autenticar(usr, pas):
        hash = hashlib.sha256(str.encode(pas))
        print(hash.hexdigest())
        consulta = Interop_CRUDS.Consultar_Uno(Usuario_Servidor(usr,pas), 'User_Name', usr)
