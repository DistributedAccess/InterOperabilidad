import jwt

class Auth_JWT:

    def Crear_Token(usr, pass):
        token = jwt.encode({'some': 'payload'}, key, algorithm='HS256')
        return token

    #DEBE CONVERTIRSE EN UN DECORADOR
    def Validar_Token(tkin):
        decoded = jwt.decode(tkin, key, algorithms='HS256')
        return decoded
