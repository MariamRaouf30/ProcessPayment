from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/processPayment", methods=["POST"])
def process_payment():
    return jsonify({
        "status": "success",
        "transaction_id": "TXN123456",
        "message": "Payment processed successfully"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
