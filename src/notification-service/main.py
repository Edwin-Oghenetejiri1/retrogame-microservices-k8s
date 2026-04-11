from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

notifications = []
notification_id_counter = 1

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "service": "notification-service"})

@app.route('/notifications', methods=['GET'])
def get_notifications():
    return jsonify(notifications)

@app.route('/notifications/<user_id>', methods=['GET'])
def get_user_notifications(user_id):
    user_notifications = [n for n in notifications if n['userId'] == user_id]
    return jsonify(user_notifications)

@app.route('/notifications/send', methods=['POST'])
def send_notification():
    global notification_id_counter
    data = request.get_json()
    notification = {
        "notificationId": notification_id_counter,
        "userId": data.get("userId"),
        "message": data.get("message"),
        "type": data.get("type", "EMAIL"),
        "status": "SENT",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notifications.append(notification)
    notification_id_counter += 1
    return jsonify(notification)

if __name__ == '__main__':
    print("Notification service starting on port 8083...")
    app.run(host='0.0.0.0', port=8083, debug=True)