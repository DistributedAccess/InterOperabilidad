import sys
sys.path.append("../..")
from Infrastructure.Logging import Logging
import zipfile
import os

logg    = Logging()

class Process_Files:
    """     Esta clase es la encargada de todo tipo de procesamiento de
            archivos, como mover, copiar, descomprimir etc...
    """

    @staticmethod
    def Descomprimir(origen, destino):
        try:
            with zipfile.ZipFile(origen, "r") as zip:
                zip.extractall(destino)
            logg.debug("Se descomprimio el archivo: " + origen)
            return True

        except Exception as e:
            logg.error("No se pudo descomprimir: " + origen)
            logg.error(e)
            return False

    @staticmethod
    def Mover_Directorio(origen, destino):
        try:
            shutil.move(origen, destino)
            logg.debug("Se movio el Directorio: " + origen + "al destino: " + destino)
            return True

        except Exception as e:
            logg.error("No se movio el Directorio: " + origen + "al destino: " + destino)
            logg.error(e)
            return False

    @staticmethod
    def Crear_Directorios(dir):
        try:
            if not os.path.exists(dir):
                os.mkdir(dir)
                logg.debug("Se creo el Directorio: " + dir)
            else:
                logg.info("Ya existe el Directorio: " + dir)
            return True

        except Exception as e:
            logg.error("No se creo el Directorio: " + dir)
            logg.error(e)
            return False

    @staticmethod
    def Delete_File(file):
        try:
            if not os.path.exists(file):
                logg.info("No existe el archivo: " + file)
            else:
                os.remove(file)
                logg.debug("Se elimino el archivo: " + file)

            return True

        except Exception as e:
            logg.error("No se elimino el archivo: " + file)
            logg.error(e)
            return False

    @staticmethod
    def Delete_Directory(dir):
        try:
            if not os.path.exists(dir):
                logg.info("No existe el Directorio: " + dir)
            else:
                os.rmdir(dir)
                logg.debug("Se elimino el Directorio: " + dir)

            return True

        except Exception as e:
            logg.error("No se elimino el Directorio: " + dir)
            logg.error(e)
            return False

    @staticmethod
    def Lst_Dir(dir):
        try:
            if not os.path.exists(dir):
                logg.info("No existe el Directorio: " + dir)
                return None
            else:
                lst = os.listdir(dir)
                logg.debug("Se obtuvo una lista del Directorio: " + dir)
                return lst

        except Exception as e:
            logg.error("No se pudo obtener una lista del Directorio: " + dir)
            logg.error(e)
            return None
