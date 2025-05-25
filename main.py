from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

signal_store = {
    "candle": "red",
    "rsi": 50.0
}

@app.route("/")
def home():
    return "TradeSense API Aktif", 200

@app.route("/sinyal", methods=["GET"])
def get_signal():
    return jsonify(signal_store), 200

@app.route("/update", methods=["POST"])
def update_signal():
    try:
        data = request.get_json(force=True)
        signal_store["candle"] = data.get("candle")
        signal_store["rsi"] = float(data.get("rsi"))
        return jsonify({"status": "ok", "data": signal_store}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run()
