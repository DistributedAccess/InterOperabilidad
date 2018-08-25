from flask import Flask, abort, request
from argparse import Namespace
import json

app = Flask(__name__)


@app.route('/Interoperabilidad/Login', methods=['POST'])
def foo():
    if not request.json:
        abort(400)

    input = json.dumps(request.json)
    print(type(input))
    data = json.loads(input)
    print(type(data))

    usersJson = data["Usuarios"]
    print(type(usersJson))

    return json.dumps(request.json)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
