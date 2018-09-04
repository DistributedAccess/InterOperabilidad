import sys
sys.path.append("../..")
from Infrastructure.Config import Config
from Infrastructure.Logging import Logging
from Business_Layer.Business_Functionalities.Process_Files import Process_Files

cnf     = Config()
config  = cnf.conf()
logg    = Logging()

faceDB = config['Directorios']['Unzip']
buzon  = config['Directorios']['BuzonSftp']

class Interop_ZipRegistrar:

    @staticmethod
    def ZipRegistrar(users):
        Valida_Directorio()

        lstJson = lst_Users(users)
        lstZip = Descomprimir_to_(users['Nombre'])

        return Respuesta(lstJson, lstZip)



def Respuesta(lstJson, lstZip):
    return Compare_lst(lstJson, lstZip)

def Valida_Directorio():
    return Process_Files.Crear_Directorios(faceDB)

def Descomprimir_to_(file):
    if(Process_Files.Descomprimir(buzon+"/"+file,faceDB)):
        return Process_Files.Lst_Dir(faceDB)
    else:
        return None

def lst_Users(users):
    lst = []
    for usr in users['Usuarios']:
        lst.append(usr['Usuario']['Id_Usuario'])
    return lst

def Compare_lst(lstJson, lstZip):
    """     Regresa una lista de los usuarios que no estan en el Zip"""
    lst =  []
    for ljsn in lstJson:
        if ljsn not in lstZip:
            lst.append((ljsn, False))
        if ljsn in lstZip:
            lst.append((ljsn, True))
    return lst
