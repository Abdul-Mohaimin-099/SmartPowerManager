import os

def set_power_mode(mode):
    if mode == "performance":
        print("Activating Performance Mode")
        os.system("powercfg /s 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")  # High Performance
    elif mode == "balanced":
        print("Activating Balanced Mode")
        os.system("powercfg /s 381b4222-f694-41f0-9685-ff5bb260df2e")  # Balanced
    elif mode == "power_saver":
        print("Activating Power Saver Mode")
        os.system("powercfg /s a1841308-3541-4fab-bc81-f71556f20b4a")  # Power Saver
    
    
