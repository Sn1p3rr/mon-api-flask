from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/deals')
def get_deals():
    deals = [
        {"nom": "Hoodie Nike Tech", "prix": "79,99€", "url": "https://nike.com/hoodie"},
        {"nom": "Cargo Adidas", "prix": "49,99€", "url": "https://adidas.fr/cargo"},
    ]
    return jsonify(deals)

if __name__ == '__main__':
    app.run()
