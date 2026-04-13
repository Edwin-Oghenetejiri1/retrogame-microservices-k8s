from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory cart storage
carts = {}

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "service": "cart-service"})

@app.route('/cart/<user_id>', methods=['GET'])
def get_cart(user_id):
    cart = carts.get(user_id, [])
    return jsonify({"user_id": user_id, "items": cart})

@app.route('/cart/<user_id>/add', methods=['POST'])
def add_to_cart(user_id):
    item = request.get_json()
    if user_id not in carts:
        carts[user_id] = []
    carts[user_id].append(item)
    return jsonify({"message": "Item added", "cart": carts[user_id]})

@app.route('/cart/<user_id>/remove', methods=['DELETE'])
def remove_from_cart(user_id):
    item_id = request.get_json().get('id')
    if user_id in carts:
        carts[user_id] = [i for i in carts[user_id] if str(i.get('id')) != str(item_id)]
    return jsonify({"message": "Item removed", "cart": carts.get(user_id, [])})

@app.route('/cart/<user_id>/clear', methods=['DELETE'])
def clear_cart(user_id):
    carts[user_id] = []
    return jsonify({"message": "Cart cleared"})

if __name__ == '__main__':
    print("Cart service starting on port 8081...")
    app.run(host='0.0.0.0', port=8081, debug=True)