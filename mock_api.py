from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔹 Mock Database (simulate real backend data)
mock_data = {
    "sub_101": {
        "customer_name": "Aman",
        "plan": "Pro",
        "status": "Active",
        "amount": 999
    },
    "sub_102": {
        "customer_name": "Rahul",
        "plan": "Basic",
        "status": "Inactive",
        "amount": 499
    }
}

# 🔹 API Endpoint
@app.route('/get-subscription', methods=['GET'])
def get_subscription():
    subscription_id = request.args.get('subscription_id')

    # Validation
    if not subscription_id:
        return jsonify({"error": "subscription_id is required"}), 400

    # Fetch data
    if subscription_id in mock_data:
        return jsonify({
            "subscription_id": subscription_id,
            "data": mock_data[subscription_id]
        })
    else:
        return jsonify({"error": "Subscription not found"}), 404


# 🔹 Run server
if __name__ == '__main__':
    app.run(debug=True)