from flask import Flask, send_from_directory
from flask_socketio import SocketIO
from monitor import get_system_status
import time
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

def background_task():
    while True:
        data = get_system_status()

        socketio.emit("update", {
            "data": data
        })

        time.sleep(3)


@app.route("/")
def index():
    return send_from_directory(os.path.dirname(__file__), "static/dashboard.html")


if __name__ == "__main__":
    socketio.start_background_task(background_task)
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)