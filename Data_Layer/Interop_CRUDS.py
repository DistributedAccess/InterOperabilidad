from mysql.connector import errorcode
import mysql.connector
import ConfigParser

class Interop_CRUDS:

    def Registrar_Usuario():
        db = MySQLdb.connect(user = self.__User, passwd = self.__Password,
                              host = '127.0.0.1',
                              db = 'CONTROL_DISTRIBUIDO')
