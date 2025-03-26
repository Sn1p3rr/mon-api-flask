from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # ← autorise toutes les origines pour /api/*

@app.route('/')
def index():
    return "API OK"

@app.route('/api/deals')
def get_deals():
    deals = [
        {"nom": "Hoodie Nike Tech", "prix": "79,99€", "url": "https://nike.com/hoodie"},
        {"nom": "Cargo Adidas", "prix": "49,99€", "url": "https://adidas.fr/cargo"},
    ]
    return jsonify(deals)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
