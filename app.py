from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "🚀 L'API est en ligne ! Va sur /api/deals pour voir les deals."

@app.route('/api/deals')
def get_deals():
    deals = [
        {"nom": "Hoodie Nike Tech", "prix": "79,99€", "url": "https://nike.com/hoodie"},
        {"nom": "Cargo Adidas", "prix": "49,99€", "url": "https://adidas.fr/cargo"},
    ]
    return jsonify(deals)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)