import os
from flask import Flask, jsonify, request

app = Flask(__name__)

carts = {}

@app.route('/cart/<user_id>', methods=['GET'])
def get_cart(user_id):
    items = carts.get(user_id, [])
    return jsonify({"items": items})


@app.route('/cart/<user_id>/add', methods=['POST'])
def add_to_cart(user_id):
    data = request.get_json(silent=True) or request.form.to_dict()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    item = {
        "id": data.get("id"),
        "name": data.get("name"),
        "price": data.get("price")
    }

    if not all([item["id"], item["name"], item["price"]]):
        return jsonify({"error": "Missing item fields"}), 400

    if user_id not in carts:
        carts[user_id] = []

    carts[user_id].append(item)

    return jsonify({"message": "Item added", "cart": carts[user_id]}), 201


@app.route('/cart/<user_id>/remove', methods=['POST'])
def remove_from_cart(user_id):
    data = request.get_json(silent=True) or request.form.to_dict()

    if data:
        item_id = data.get('id')
        if user_id in carts:
            carts[user_id] = [
                i for i in carts[user_id]
                if str(i.get('id')) != str(item_id)
            ]

    return jsonify({"message": "Item removed", "cart": carts.get(user_id, [])})


@app.route('/cart/<user_id>/clear', methods=['DELETE'])
def clear_cart(user_id):
    carts[user_id] = []
    return jsonify({"message": "Cart cleared"})


if __name__ == '__main__':
    print("Cart service starting on port 8081...")

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8081"))

    app.run(host=host, port=port, debug=False)









