import sys
sys.path.append("..")
from flask import Flask, abort, request
from argparse import Namespace
from Business_Layer.Business_Api.Interop_Login import *
from Business_Layer.Business_Api.Interop_Registrar import *
from Infrastructure.Auth_JWT import Auth_JWT
import json

app = Flask(__name__)

@app.route('/Interoperabilidad/Login', methods=['POST'])
def Login():
    if not request.json:
        abort(400)
    return Interop_Login.Interop_Login(request.json)

@app.route('/Interoperabilidad/Registrar', methods=['POST'])
def Registrar():
    if not request.json:
        abort(400)
    token = request.headers.get('Authorization')
    token = token.replace('Bearer ','')

    #@Auth_JWT.Validar_Token(token)
    return Interop_Registrar.Registrar_Usuarios(request.json)


@app.route('/Interoperabilidad/Consultar', methods=['GET'])
def Id_Usuario():
    if 'Id' in request.args:
        return request.args['Id']
    else:
        return "No tienes idea"

@app.route('/Interoperabilidad/Actualizar', methods=['PUT'])
def fooq():
    if not request.json:
        abort(400)

    input = json.dumps(request.json)
    data = json.loads(input)

    return json.dumps(request.json)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
