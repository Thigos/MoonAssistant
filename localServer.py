from flask import Flask, jsonify, request
from MoonAssistant import MoonAssistant
from DBConnection import DBConnection

app = Flask(__name__)
moonAssistant = MoonAssistant()
dbConnection = DBConnection()

@app.route('/MoonAssistant/send', methods=['POST'])
def send():
    data = request.get_json()
    message = data['message']
    idUsuario = data['idUsuario']

    response = moonAssistant.send(message)

    json = {
        'content':response['content'],
        'images':response['images'] if 'images' in response.keys() else [],
        'links':response['links'] if 'links' in response.keys() else [],
    }

    dbConnection.writeDB({
        'content': message,
        'images': [],
        'links': [],
    }, idUsuario, False)

    dbConnection.writeDB(json, idUsuario, True)

    return jsonify(json)

if __name__ == '__main__':
    app.run(debug=False, port=5555)
