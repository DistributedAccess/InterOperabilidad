#from DTO import *
#import sys
#sys.path.append("..")
from Infrastructure.Config import Config
from Infrastructure.Logging import Logging
import MySQLdb

cnf     = Config()
config  = cnf.conf()
logg    = Logging()

class Interop_CRUDS:

    @staticmethod
    def Registrar_Actualizar(dto):
        pass

    @staticmethod
    def Registrar(dto):
        columns, values = Query_Insert(dto)
        query = "INSERT INTO " + type(dto).__name__ +  columns + " VALUES " + values
        if(Execute_Query(query)):
            logg.debug("Se ha registrado un registro a la tabla: " + type(dto).__name__)
        else:
            logg.error("No se ha registrado un registro a la tabla: " + type(dto).__name__)

    @staticmethod
    def Actualizar(dto, condicion, parametro):
        set = Query_Update(dto)
        query = "UPDATE " + type(dto).__name__ + " SET " + set + " WHERE " + condicion + " = " + "'" + parametro + "'"
        if(Execute_Query(query)):
            logg.debug("Se ha actualizado un registro a la tabla: " + type(dto).__name__)
        else:
            logg.debug("No se ha registrado un registro a la tabla: " + type(dto).__name__)

    @staticmethod
    def Consultar_Uno(dto, columna, condicion):
        query = "SELECT * FROM " + type(dto).__name__ + " WHERE " + columna +" = '" + condicion + "'"
        consulta = Execute_Query_Consultar(query)
        if(len(consulta) != 0):
            logg.debug("Se ha registrado un registro a la tabla: " + type(dto).__name__)
        else:
            logg.debug("No se ha registrado un registro a la tabla: " + type(dto).__name__)
        return  consulta

    @staticmethod
    def Consultar_Todo(dto):
        query = "SELECT * FROM " + type(dto).__name__
        consulta = Execute_Query_Consultar(query)
        if(len(consulta) != 0):
            logg.debug("Se ha registrado un registro a la tabla: " + type(dto).__name__)
        else:
            logg.debug("No se ha registrado un registro a la tabla: " + type(dto).__name__)
        return  consulta

def Execute_Query(query):
    db      = None
    cursor  = None
    try:
        db = MySQLdb.connect(user = config['MySql']['User'],
                             passwd = config['MySql']['Password'],
                             host = config['MySql']['Host'],
                             db = config['MySql']['DataBase'])

        cursor = db.cursor()
        print(query)
        logg.debug("Se ha establecido a la base de datos: " + config['MySql']['DataBase'])
        cursor.execute(query)
        db.commit()
        cursor.close()
        return True

    except Exception as e:
        print(e)
        cursor.close()
        logg.error("No se ha podido conectar a la de base de datos: " + config['MySql']['DataBase'])
        return False

def Execute_Query_Consultar(query):
    db      = None
    cursor  = None
    try:
        db = MySQLdb.connect(user = config['MySql']['User'],
                             passwd = config['MySql']['Password'],
                             host = config['MySql']['Host'],
                             db = config['MySql']['DataBase'])

        cursor = db.cursor()
        logg.debug("Se ha establecido a la base de datos: " + config['MySql']['DataBase'])
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    except Exception as e:
        print(e)
        cursor.close()
        logg.error("No se ha podido conectar a la de base de datos: " + config['MySql']['DataBase'])
        return None

def Query_Insert(dto):
    columns = " ("
    values  = "("
    lista = Lista_Atributos(dto)

    l = len(lista)
    c = 0
    for lst in lista:
        c += 1
        columns  +=  lst
        if(getattr(dto, lst) == ""):
            values += "NULL"
        elif(str(getattr(dto, lst)).lower() == "true"):
            values += "TRUE"
        elif(str(getattr(dto, lst)).lower() == "false"):
            values += "FALSE"
        elif(getattr(dto, lst).isdigit()):
            values += getattr(dto, lst)
        else:
            values   +=  "'" + getattr(dto, lst) + "'"
        if(c != l):
            columns += ","
            values  += ","

    columns  += ")"
    values   += ")"

    return columns, values

def Query_Update(dto):
    set = ""
    lista = Lista_Atributos(dto)

    l = len(lista)
    c = 0
    for lst in lista:
        c += 1

        if(getattr(dto, lst) == ""):
            set += lst + " = " + "NULL, "
        elif(getattr(dto, lst) == "True"):
            set += lst + " = " + "TRUE, "
        elif(getattr(dto, lst) == "False"):
            set += lst + " = " + "FALSE, "
        elif(getattr(dto, lst).isdigit()):
            set += lst + " = " + getattr(dto, lst) + ", "
        else:
            set += lst + " = '" + getattr(dto, lst)

            if(c != l):
                set += "', "
            else:
                set += "'"

    return set

def Lista_Atributos(dto):
    lsta = []
    for lst in dir(dto):
        if '__' not in lst:
            lsta.append(lst)
    return lsta
