from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔹 Mock Database (based on your actual schema)
mock_data = {
    "dc5dde69-fe06-4937-ad19-bb58d6e16b0d": {
        "customer_mobile_number": "8879194838",
        "activated_date": "1-Feb-26",
        "expiry_date": "02-01-2028",
        "duration_in_days": 730,
        "invoice_number": "MBB/25-26/93747",
        "amount": 800,
        "plan": "silver",
        "transaction_id": "order_SAcBajIngEuW3z",
        "business": 1,
        "users": 1,
        "first_name": "Cloth Factory",
        "platform": "mobile",
        "activated_timestamp": "2026-02-01 14:48:43",
        "subscription_id": "dc5dde69-fe06-4937-ad19-bb58d6e16b0d"
    },
    "0eb11c6d-e128-4971-9ce1-d91246ff1207": {
        "customer_mobile_number": "7002857826",
        "activated_date": "1-Feb-26",
        "expiry_date": "02-01-2027",
        "duration_in_days": 365,
        "invoice_number": "MBB/25-26/93788",
        "amount": 471,
        "plan": "silver",
        "transaction_id": "order_SAnTVmivdxChcg",
        "business": 1,
        "users": 1,
        "first_name": "Your Name",
        "platform": "mobile",
        "activated_timestamp": "2026-02-01 12:52:13",
        "subscription_id": "0eb11c6d-e128-4971-9ce1-d91246ff1207"
    }
    # Add more rows similarly if needed
}

# 🔹 API Endpoint
@app.route('/get-subscription', methods=['GET'])
def get_subscription():
    subscription_id = request.args.get('subscription_id').strip()
    
    print("🔥 NEW CODE RUNNING 🔥")
    if not subscription_id:
        return jsonify({"error": "subscription_id is required"}), 400

    if subscription_id in mock_data:
        return jsonify(mock_data[subscription_id])
    else:
        return jsonify({"error": "Subscription not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
