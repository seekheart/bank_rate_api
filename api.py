from flask import Flask, jsonify
from flask_cors import CORS
from engines import BankRateEngine

app = Flask('__name__')
CORS(app)
bank_rate_engine = BankRateEngine()


@app.route('/rates', methods=['GET'])
def get_rates():
    return jsonify(bank_rate_engine.find_all())


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=3000,
        debug=False,
        threaded=True
    )