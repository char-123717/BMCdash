import psutil
import time

history = {
    "cpu": [],
}

def get_system_status():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # 保留 history（最多 600 筆）
    history["cpu"].append(cpu)
    if len(history["cpu"]) > 600:
        history["cpu"].pop(0)

    return {
        "cpu": cpu,
        "memory": mem,
        "disk": disk,
        "history": history
    }