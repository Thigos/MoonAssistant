from flask import Flask, jsonify, request
from MoonAssistant import MoonAssistant

app = Flask(__name__)
moonAssistant = MoonAssistant()

@app.route('/MoonAssistant/send', methods=['POST'])
def hello():
    data = request.get_json()
    
    message = data['message']

    response = moonAssistant.send(message)

    return jsonify({
        'content':response['content'],
        'images':response['images'] if 'images' in response.keys() else [],
        'links':response['links'] if 'links' in response.keys() else [],
    })

if __name__ == '__main__':
    app.run(debug=False, port=5555)
