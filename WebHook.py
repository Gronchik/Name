from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.json
    # Обработка обновления
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run()