from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

@app.route('/processPayment', methods=['POST'])
def process_payment():
    data = request.get_json()

    required_fields = ['from_account', 'store_code', 'amount', 'currency']
    if not all(field in data for field in required_fields):
        return jsonify({
            "status": "error",
            "message": "Missing required fields"
        }), 400

    # Dummy logic
    transaction_id = f"TXN{uuid.uuid4().hex[:10].upper()}"

    return jsonify({
        "status": "success",
        "transaction_id": transaction_id,
        "message": "Payment processed successfully"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
