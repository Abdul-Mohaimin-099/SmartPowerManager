import psutil
import os

def get_cpu_usage():
    """
    Get the current CPU usage as a percentage.
    """
    return psutil.cpu_percent(interval=1)

def get_battery_status():
    """
    Get the battery status, including percentage and charging state.
    """
    battery = psutil.sensors_battery()
    return {
        "percent": battery.percent if battery else 0,
        "charging": battery.power_plugged if battery else False,
    }
def get_disk_usage():
    """
    Get disk usage information.
    """
    disk = psutil.disk_usage('/')
    return {
        "total": round(disk.total / (1024 ** 3), 2),  # Convert total size to GB
        "used": round(disk.used / (1024 ** 3), 2),    # Convert used space to GB
        "percent": disk.percent                       # Used space as percentage
    }


def get_network_upload_speed():
    """
    Get current network upload speed.
    """
    net_before = psutil.net_io_counters()
    psutil.time.sleep(1)  # Wait for 1 second
    net_after = psutil.net_io_counters()

    upload_speed = (net_after.bytes_sent - net_before.bytes_sent) / 1024  # Convert to KB
    return upload_speed

def set_power_mode(mode):
    """
    Set the power mode to Performance, Balanced, or Power Saver.

    :param mode: str - One of "Performance", "Balanced", or "Power Saver"
    """
    if os.name == "nt":  # Windows
        if mode == "Performance":
            os.system("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")  # High Performance GUID
        elif mode == "Balanced":
            os.system("powercfg /setactive a1841308-3541-4fab-bc81-f71556f20b4a")  # Power Saver GUID
        elif mode == "Power Saver":
            os.system("powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e")  # Balanced GUID

def get_running_processes_with_resources():
    """
    Fetch the list of running processes with their PID, name, CPU%, and memory%.
    """
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append({
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "cpu_percent": proc.info['cpu_percent'],
                "memory_percent": proc.info['memory_percent'],
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return processes

