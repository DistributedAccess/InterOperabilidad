import sys
sys.path.append("..")
from flask import Flask, abort, request
from argparse import Namespace
from Data_Layer.Interop_Create_DB import *
from Infrastructure.Config import Config
from Infrastructure.Logging import Logging
import commads
import json

"""     Esta clase es la encargada de pedir al sitio de administracion
    un inicio de sesion enviandole asi las credenciales de la terminal
    de acceso, como las de rest y sftp.
"""

cnf     = Config()
config  = cnf.conf()
logg    = Logging()

if __name__ == '__main__':
    main()

def main():
    pass

def Request():
    return request =
    {
        "User": config['Admin_Rest']['AdminUser'],
        "Passwd": config['Admin_Rest']['AdminPass']
        "ControlAcceso":
        {
            "Api":
            {
                "Url":    "http://" + Ip_Host() + "//" + config['Api_Sftp']['ApiUrl'],
                "User":   config['Api_Sftp']['ApiUser'],
                "Passwd": config['Api_Sftp']['ApiPass']
            }
            "Sftp":
            {
                "Url":      Ip_Host(),
                "User":     config['Api_Sftp']['SftpUser'],
                "Passwd":   config['Api_Sftp']['SftpPass'],
                "Ruta":     config['Api_Sftp']['SftpRuta']
            }
        }
    }

def Ip_Host(self):
        Ip = commands.getoutput("hostname -I")
        Espacio = Ip.find(" ")
        Ip = Ip[0:Espacio]
        return Ip
