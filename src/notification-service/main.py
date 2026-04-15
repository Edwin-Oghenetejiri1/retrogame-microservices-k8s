import os
from flask import Flask, jsonify, request
from datetime import datetime, timezone

app = Flask(__name__)

notifications = []
notification_id_counter = 1

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

@app.route('/notifications', methods=['GET'])
def get_notifications():
    return jsonify(notifications)

@app.route('/notifications/<user_id>', methods=['GET'])
def get_user_notifications(user_id):
    return jsonify([n for n in notifications if n['userId'] == user_id])

@app.route('/notifications/send', methods=['POST'])
def send_notification():
    global notification_id_counter

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "invalid request"}), 400

    notification = {
        "notificationId": notification_id_counter,
        "userId": data.get("userId"),
        "message": data.get("message"),
        "type": data.get("type", "EMAIL"),
        "status": "SENT",
        "createdAt": datetime.now(timezone.utc).isoformat()
    }

    notifications.append(notification)
    notification_id_counter += 1

    return jsonify(notification)

if __name__ == '__main__':
    print("Notification service starting...")

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8083"))

    app.run(host=host, port=port, debug=False)