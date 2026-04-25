# 🖥️ Linux Server Health Monitor (BMC-like System)

A lightweight BMC-like system built with Python, Flask, and WebSocket to simulate real-time server health monitoring, including CPU, memory, and disk usage visualization.

---

## 🚀 Features

- 📊 Real-time system monitoring (CPU / Memory / Disk)
- 🔄 Live updates using WebSocket (no refresh needed)
- ⚠️ Alert system for high resource usage
- 📈 Simple CPU history visualization
- 🌐 Web dashboard for system status
- 🧠 Simulates basic BMC (Baseboard Management Controller) behavior

---

## 🧠 Tech Stack

- Python
- Flask
- Flask-SocketIO
- psutil
- HTML / CSS / JavaScript

---

## 🏗️ Project Structure
```

linux-bmc-monitor/
│
├── app.py              # Flask + WebSocket server
├── monitor.py          # System metrics collector
├── static/
│ └── dashboard.html    # Frontend dashboard UI


```
---

## ⚙️ Installation

### 1. Clone repository
```bash
git clone https://github.com/char-123717/BMCdash.git
```
### 2. Install dependencies
```
pip install flask flask-socketio psutil
```
### 3. Run Project
```
python app.py
```

Then open browser:
```
http://127.0.0.1:5000/static/dashboard.html
```

### 📡 API Endpoint

Get system status
GET /api/status

Example response:
```
{
  "cpu": 35.2,
  "memory": 62.1,
  "disk": 70.5
}
```

### 🧠 Architecture Overview
```
System Metrics (psutil)
        ↓
Python Backend (Flask)
        ↓
WebSocket (real-time push)
        ↓
Frontend Dashboard
        ↓
Live Monitoring UI
```

### ⚠️ Alert System

Triggers alert when:

CPU > 80%
Memory > 80%
Disk > 80%

### 🎯 Purpose

This project is built to simulate basic BMC (Baseboard Management Controller) concepts:

Server health monitoring
Remote status visibility
Real-time system updates

It helps in understanding how enterprise server management systems (e.g., iLO / iDRAC) work at a simplified level.


### 📌 Future Improvements
🔐 Login authentication (like real BMC)
📡 Redfish API simulation
📊 Chart.js advanced visualization
🐳 Docker deployment
🖥️ Multi-server monitoring
👨‍💻 Author

Built by a Computer Science student exploring systems, Linux, and backend engineering.

### 📜 License

This project is for educational purposes.