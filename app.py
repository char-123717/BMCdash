from flask import Flask
from flask_socketio import SocketIO
from monitor import get_system_status
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

def background_task():
    while True:
        data = get_system_status()

        alert = (
            data["cpu"] > 80 or
            data["memory"] > 80 or
            data["disk"] > 80
        )

        socketio.emit("update", {
            "data": data,
            "alert": alert
        })

        time.sleep(3)


@app.route("/")
def index():
    return "BMC Monitor Running"


if __name__ == "__main__":
    socketio.start_background_task(background_task)
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)