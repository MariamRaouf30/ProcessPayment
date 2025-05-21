from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/processPayment", methods=["POST"])
def process_payment():
    # Accept either JSON or form-data (x-www-form-urlencoded)
    data = request.get_json(silent=True)
    if data is None:
        data = request.form

    from_account = data.get("from_account")
    store_code = data.get("store_code")
    amount = data.get("amount")
    currency = data.get("currency")

    # Check for missing fields
    if not all([from_account, store_code, amount, currency]):
        return jsonify({
            "status": "error",
            "message": "Missing required fields"
        }), 400

    # Dummy transaction logic
    transaction_id = "TXN123456"

    return jsonify({
        "status": "success",
        "transaction_id": transaction_id,
        "message": "Payment processed successfully"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
