from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

notifications = []
notification_id_counter = 1

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/notifications/send', methods=['POST'])
def send_notification():
    global notification_id_counter

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "invalid request"}), 400

    user_id = data.get("userId")
    message = data.get("message")

    if not isinstance(user_id, int) or not message:
        return jsonify({"error": "invalid input"}), 400

    notification = {
        "notificationId": notification_id_counter,
        "userId": user_id,
        "message": message,
        "status": "SENT",
        "createdAt": datetime.utcnow().isoformat()
    }

    notifications.append(notification)
    notification_id_counter += 1

    return jsonify(notification)

if __name__ == '__main__':
    print("Notification service running...")
    app.run(host='127.0.0.1', port=8083, debug=False)