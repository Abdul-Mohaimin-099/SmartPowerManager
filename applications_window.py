from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from resource_monitor import get_running_processes_with_resources

class ApplicationsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Power Manager - Running Applications")
        self.setGeometry(100, 100, 600, 400)

        self.init_ui()

        # Timer to refresh the process list every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_process_list)
        self.timer.start(1000)

    def init_ui(self):
        layout = QVBoxLayout()

        self.process_table = QTableWidget()
        self.process_table.setColumnCount(4)
        self.process_table.setHorizontalHeaderLabels(["PID", "Name", "CPU%", "Memory%"])
        layout.addWidget(self.process_table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_process_list(self):
        processes = get_running_processes_with_resources()
        self.process_table.setRowCount(len(processes))
        for row, proc in enumerate(processes):
            self.process_table.setItem(row, 0, QTableWidgetItem(str(proc['pid'])))
            self.process_table.setItem(row, 1, QTableWidgetItem(proc['name']))
            self.process_table.setItem(row, 2, QTableWidgetItem(f"{proc['cpu_percent']}%"))
            self.process_table.setItem(row, 3, QTableWidgetItem(f"{proc['memory_percent']:.2f}%"))
