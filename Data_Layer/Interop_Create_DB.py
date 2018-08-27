import sys
sys.path.append("..")
from Infrastructure.Logging import Logging
import MySQLdb

"""   Esta clase se encarga de crear la base de datos y las tablas
      a usar en las terminales de acceso. Esta clase se ejecutara
      una sola vez solo en la instalacion de nuevas terminales.

      La Base de Datos a crear tiene las siguientes  caracteristicas:

      Base de Datos:  InterOperabilidad

      Tablas:       Usuario         -------> Tabla Catalogos
                    Horario         -------> Tabla Catalogos
                    Bitacora        -------> Tabla Historica
                    Usuario_Horario -------> Tabla Relacional


      Usuario
      +------------+------------------+------+-----+---------+----------------+
      | Field      | Type             | Null | Key | Default | Extra          |
      +------------+------------------+------+-----+---------+----------------+
      | Id_Usuario | int(10)          | NO   | PRI | NULL    |                |
      | Nombre     | varchar(50)      | NO   |     | NULL    |                |
      | Apellido_P | varchar(50)      | NO   |     | NULL    |                |
      | Apellido_M | varchar(50)      | NO   |     | NULL    |                |
      | Tipo_Usr   | varchar(50)      | NO   |     | NULL    |                |
      | Activo     | bit              | NO   |     | NULL    |                |
      +------------+------------------+------+-----+---------+----------------+
      Horario
      +------------+-------------+------+-----+---------+-------+
      | Field      | Type        | Null | Key | Default | Extra |
      +------------+-------------+------+-----+---------+-------+
      | Id_Horario | int(10)     | NO   | PRI | NULL    |       |
      | Turno      | varchar(25) | NO   |     | NULL    |       |
      | Inicio     | datetime    | NO   |     | NULL    |       |
      | Fin        | datetime    | NO   |     | NULL    |       |
      | Dia        | varchar(25) | NO   |     | NULL    |       |
      +------------+-------------+------+-----+---------+-------+
      Bitacora
      +--------------+-------------+------+-----+---------+-------+
      | Field        | Type        | Null | Key | Default | Extra |
      +--------------+-------------+------+-----+---------+-------+
      | Id_Bitacora  | int(10)     | NO   |     | NULL    |       |
      | Id_Usuario   | int(10)     | NO   |     | NULL    |       |
      | Hora_Entrada | datetime    | NO   |     | NULL    |       |
      | Turno        | varchar(25) | NO   |     | NULL    |       |
      | Asistencia   | bit         | NO   |     | NULL    |       |
      +--------------+-------------+------+-----+---------+-------+
      Usuario_Horario
      +------------+-------------+------+-----+---------+-------+
      | Field      | Type        | Null | Key | Default | Extra |
      +------------+-------------+------+-----+---------+-------+
      | Id_UsrHora | int(10)     | NO   | PRI | NULL    |       |
      | Id_Horario | int(10)     | NO   | FOR | NULL    |       |
      | Id_Usuario | int(10)     | NO   | FOR | NULL    |       |
      +------------+-------------+------+-----+---------+-------+
"""

class Interop_Create_DB:

    __user      = None
    __password  = None
    __host      = None
    __dataBase  = None

    __db        = None
    __cursor    = None

    __logg = Logging()

    def __init__(self, user, passwd, host, db):
        self.__user     = user
        self.__password = passwd
        self.__host     = host
        self.__dataBase = db

        try:
            self.__db = MySQLdb.connect(user = self.__user, passwd = self.__password)
            self.__cursor = self.__db.cursor()
            self.__logg.debug("Se ha establecido la conexion al motor de base de datos")

        except Exception as e:
            self.__logg.error("No se ha podido conectar al motor de base de datos ")


    def Create_DataBase(self):
        #   Este metodo crea la Base de Datos InterOperabilidad.
        try:
            sql = "CREATE DATABASE IF NOT EXISTS InterOperabilidad"
            self.__cursor.execute(sql)
            self.__logg.debug("Se ha creado la Base de Datos: Interoperabilidad")

        except  MySQLdb.DatabaseError:
            self.__logg.error("No se ha podido crear la Base de datos: Interoperabilidad")

    def Conectar_Base(self):
        #   Este metodo se conecta a la base de Datos Interoperabilidad
        try:
            self.__db = MySQLdb.connect(user = self.__user, passwd = self.__password,
                                        host = '127.0.0.1',
                                        db = "InterOperabilidad")

            self.__cursor = self.__db.cursor()
            self.__logg.debug("Se ha establecido a la base de datos: InterOperabilidad")

        except Exception as e:
            self.__logg.error("No se ha podido conectar a la de base de datos: InterOperabilidad")

    def Create_Usuario(self):
        #   Este metodo crea la tabla: Tipo_UsrUsuario
        #   de la Base de Datos InterOperabilidad

        try:
            QUERY = ("""CREATE TABLE IF NOT EXISTS Usuario (
                    Id_Usuario int(10) NOT NULL,
                    Nombre varchar(50) NOT NULL,
                    Apellido_P varchar(50) NOT NULL,
                    Apellido_M varchar(50) NOT NULL,
                    Tipo_Usr varchar(50) NOT NULL,
                    Activo bit NOT NULL,
                    PRIMARY KEY (Id_Usuario)
                    )""")

            self.__cursor.execute(QUERY)
            self.__logg.debug("Se ha creado la Tabla: Usuario en la base de datos InterOperabilidad")

        except  MySQLdb.DatabaseError:
            self.__logg.error("No se ha podido crear la Tabla: Usuario")

    def Create_Horario(self):
        #   Este metodo crea la tabla: Horario
        #   de la Base de Datos InterOperabilidad

        try:
            QUERY = ("""CREATE TABLE IF NOT EXISTS Horario (
                    Id_Horario int(10) NOT NULL,
                    Turno varchar(25) NOT NULL,
                    Inicio datetime NOT NULL,
                    Fin datetime NOT NULL,
                    Dia varchar(25) NOT NULL,
                    PRIMARY KEY (Id_Horario)
                    )""")

            self.__cursor.execute(QUERY)
            self.__logg.debug("Se ha creado la Tabla: Horario en la base de datos InterOperabilidad")

        except  MySQLdb.DatabaseError:
            self.__logg.error("No se ha podido crear la Tabla: Horario")

    def Create_Bitacora(self):
        #   Este metodo crea la tabla: Bitacora
        #   de la Base de Datos InterOperabilidad

        try:
            QUERY = ("""CREATE TABLE IF NOT EXISTS Bitacora (
                    Id_Bitacora int(10) NOT NULL,
                    Id_Usuario int(10) NOT NULL,
                    Hora_Entrada datetime NOT NULL,
                    Turno varchar(25) NOT NULL,
                    Asistencia bit NOT NULL
                    )""")

            self.__cursor.execute(QUERY)
            self.__logg.debug("Se ha creado la Tabla: Bitacora en la base de datos InterOperabilidad")

        except  MySQLdb.DatabaseError:
            self.__logg.error("No se ha podido crear la Tabla: Bitacora")

    def Create_Usuario_Horario(self):
        #   Este metodo crea la tabla: Usuario_Horario
        #   de la Base de Datos InterOperabilidad

        try:
            QUERY = ("""CREATE TABLE IF NOT EXISTS Usuario_Horario (
                    Id_UsrHora int(10) NOT NULL,
                    Id_Horario int(10) NOT NULL,
                    Id_Usuario int(10) NOT NULL,
                    PRIMARY KEY (Id_UsrHora),
                    FOREIGN KEY (Id_Horario) REFERENCES Horario(Id_Horario),
                    FOREIGN KEY (Id_Usuario) REFERENCES Usuario(Id_Usuario)
                    )""")

            self.__cursor.execute(QUERY)
            self.__logg.debug("Se ha creado la Tabla: Usuario_Horario en la base de datos InterOperabilidad")

        except  MySQLdb.DatabaseError:
            self.__logg.error("No se ha podido crear la Tabla: Usuario_Horario")

    def Cerrar_Conexion(self):
        #   Este metodo cierra la conexion al motor de base de datos
        try:
            self.__db.close()
            self.__logg.debug("Se ha cerrado la conexion al motor de base de datos")
        except:
            self.__logg.debug("No se ha podido cerrar la conexion al motor de base de datos")
