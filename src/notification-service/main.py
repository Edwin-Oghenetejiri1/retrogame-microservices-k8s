import os
from flask import Flask, jsonify, request
from datetime import datetime, timezone

app = Flask(__name__)

notifications = []
notification_id_counter = 1


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "notification-service"
    })


@app.route('/notifications', methods=['GET'])
def get_notifications():
    return jsonify(notifications)


@app.route('/notifications/<user_id>', methods=['GET'])
def get_user_notifications(user_id):
    user_notifications = [
        n for n in notifications if str(n.get('userId')) == str(user_id)
    ]
    return jsonify(user_notifications)


@app.route('/notifications/send', methods=['POST'])
def send_notification():
    global notification_id_counter

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "invalid request"}), 400

    user_id = data.get("userId")
    message = data.get("message")
    notif_type = data.get("type", "EMAIL")

    if user_id is None or message is None:
        return jsonify({"error": "missing fields"}), 400

    notification = {
        "notificationId": notification_id_counter,
        "userId": user_id,
        "message": message,
        "type": notif_type,
        "status": "SENT",
        "createdAt": datetime.now(timezone.utc).isoformat()
    }

    notifications.append(notification)
    notification_id_counter += 1

    return jsonify(notification), 201


@app.route('/notifications/clear', methods=['DELETE'])
def clear_notifications():
    global notifications
    notifications = []
    return jsonify({"message": "all notifications cleared"})


if __name__ == '__main__':
    print("Notification service starting on port 8083...")

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8083"))

    app.run(host=host, port=port, debug=False)










