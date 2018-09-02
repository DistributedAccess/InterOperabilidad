import jwt

class Auth_JWT:

    @staticmethod
    def Crear_Token(usr, pas):
        key = "I will always love you"
        token = jwt.encode({'some': 'payload'}, key, algorithm='HS256')
        return token.decode(encoding="utf-8")

    #DEBE CONVERTIRSE EN UN DECORADOR
    def Validar_Token(tkin):
        decoded = jwt.decode(tkin, key, algorithms='HS256')
        return decoded
