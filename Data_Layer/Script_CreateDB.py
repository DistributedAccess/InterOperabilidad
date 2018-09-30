import sys
sys.path.append("..")
from Infrastructure.Config import Config
from Infrastructure.Logging import Logging
from Interop_Create_DB import Interop_Create_DB

"""         Esta clase se encarga unicamente de llamar la clase
        Interop_Create_DB para crear la base de datos y sus respectivas
        tablas, ademas de ingresar el usuario de configuracion...
"""

user   = config['MySql']['User']
passwd = config['MySql']['Password']
host   = config['MySql']['Host']
db     = config['MySql']['DataBase']

if __name__ == '__main__':
    BD = Interop_Create_DB(user, passwd, host, db)
    BD.Create_DataBase()
    BD.Conectar_Base()
    BD.Create_Usuario()
    BD.Create_Horario()
    BD.Create_Bitacora()
    BD.Create_Usuario_Horario()
    BD.Create_Usuario_Servidor()
    BD.Cerrar_Conexion()
