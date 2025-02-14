from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import QTimer
from resource_monitor import get_cpu_usage, get_battery_status, get_disk_usage, get_network_upload_speed, set_power_mode


class CPUBatteryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Power Manager - CPU, Battery, Disk, and Network Stats")
        self.setGeometry(100, 100, 500, 400)

        self.init_ui()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)  # Update every second

    def init_ui(self):
        layout = QVBoxLayout()

        # CPU and Battery Stats
        self.cpu_label = QLabel("CPU Usage: --%")
        self.cpu_label.setStyleSheet("font-size: 16px; color: #333;")
        layout.addWidget(self.cpu_label)

        self.battery_label = QLabel("Battery: --%")
        self.battery_label.setStyleSheet("font-size: 16px; color: #333;")
        layout.addWidget(self.battery_label)

        # Disk Usage
        self.disk_label = QLabel("Disk Usage: --")
        self.disk_label.setStyleSheet("font-size: 16px; color: #333;")
        layout.addWidget(self.disk_label)

        # Network Upload Speed
        self.upload_label = QLabel("Upload Speed: --")
        self.upload_label.setStyleSheet("font-size: 16px; color: #333;")
        layout.addWidget(self.upload_label)
        # Power Mode Buttons
        button_layout = QHBoxLayout()
        performance_button = QPushButton("Performance Mode")
        performance_button.setStyleSheet("background-color: #F44336; color: white; padding: 10px; font-size: 14px;")
        performance_button.clicked.connect(lambda: self.change_power_mode("Performance"))

        balanced_button = QPushButton("Balanced Mode")
        balanced_button.setStyleSheet("background-color: #FFC107; color: black; padding: 10px; font-size: 14px;")
        balanced_button.clicked.connect(lambda: self.change_power_mode("Balanced"))
        power_saver_button = QPushButton("Power Saver Mode")
        power_saver_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; font-size: 14px;")
        power_saver_button.clicked.connect(lambda: self.change_power_mode("Power Saver"))
        button_layout.addWidget(performance_button)
        button_layout.addWidget(balanced_button)
        button_layout.addWidget(power_saver_button)

        layout.addLayout(button_layout)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    def update_stats(self):
        cpu = get_cpu_usage()
        battery = get_battery_status()
        disk = get_disk_usage()
        upload_speed = get_network_upload_speed()
        self.cpu_label.setText(f"CPU Usage: {cpu}%")
        charging_status = "Charging" if battery["charging"] else "Not Charging"
        self.battery_label.setText(f"Battery: {battery['percent']}% ({charging_status})")
        self.disk_label.setText(f"Disk Usage: {disk['used']} GB / {disk['total']} GB ({disk['percent']}%)")
        self.upload_label.setText(f"Upload Speed: {upload_speed:.2f} KB/s")
    def change_power_mode(self, mode):
        set_power_mode(mode)
        self.statusBar().showMessage(f"Switched to {mode} mode", 3000)
