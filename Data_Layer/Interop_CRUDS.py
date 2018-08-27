from DTO import *
import MySQLdb

class Interop_CRUDS:

    @staticmethod
    def Registrar_Actualizar(dto):
        pass

    @staticmethod
    def Create_Query(dto):
        values = "("
        valuess = "("
        lista = Lista_Atributos(dto)
        print(lista)
        for lst in lista:
            print(lst)
            values  += lst + ","
            valuess += getattr(dto, lst) + ","
            print(valuess)
        values  += ")"
        valuess += ")"
        print (values)
        print (valuess)

def Lista_Atributos(dto):
    lsta = []
    for lst in dir(dto):
        if '__' not in lst:
            lsta.append(lst)
    return lsta
