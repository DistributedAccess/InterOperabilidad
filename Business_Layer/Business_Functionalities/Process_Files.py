import configparser
import zipfile
import os

class Process_Files:
    """     Esta clase es la encargada de todo tipo de procesamiento de
            archivos, como mover, copiar, descomprimir etc...
    """

    @staticmethod
    def Descomprimir(origen, destino):
        try:

            with zipfile.ZipFile(origen, "r") as zip:
                zip.extractall(destino)

            print("Se descomprimio el archivo: " + origen)
            return True

        except Exception as e:

            print("No se pudo descomprimir: " + origen)
            print(e)

            return False

    @staticmethod
    def Mover_Directorio(origen, destino):
        try:

            shutil.move(origen, destino)

            return True

        except Exception as e:

            print("No se pudo mover el Directorio: " + origen)
            print(e)

            return False

    @staticmethod
    def Crear_Directorios():


    @staticmethod
    def Leer_Config():
        parser = configparser.ConfigParser()
        parser.read('/home/parzival/Documents/Tesis/API/InterOperabilidad_API/config.ini')
        print(parser.sections())
        print(parser.get('MySql','User'))
