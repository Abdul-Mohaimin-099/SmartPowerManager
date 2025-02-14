from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from cpu_battery_window import CPUBatteryWindow
from graph_window import GraphWindow
from applications_window import ApplicationsWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Power Manager - Home")
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QIcon("app_icon.ico"))

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Header
        header = QLabel("Smart Power Manager")
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: #4CAF50; margin: 10px;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # Button Container
        button_layout = QHBoxLayout()

        # CPU & Battery Stats Button
        cpu_battery_button = QPushButton("CPU & Battery Stats")
        cpu_battery_button.setIcon(QIcon("icons/cpu.png"))
        cpu_battery_button.setStyleSheet(
            "background-color: #FF5733; color: white; font-size: 14px; padding: 10px; border-radius: 5px;"
        )
        cpu_battery_button.clicked.connect(self.open_cpu_battery_window)

        # Graph Button
        graph_button = QPushButton("Graphs")
        graph_button.setIcon(QIcon("icons/graph.png"))
        graph_button.setStyleSheet(
            "background-color: #33A1FF; color: white; font-size: 14px; padding: 10px; border-radius: 5px;"
        )
        graph_button.clicked.connect(self.open_graph_window)

        # Running Applications Button
        applications_button = QPushButton("Running Applications")
        applications_button.setIcon(QIcon("icons/applications.png"))
        applications_button.setStyleSheet(
            "background-color: #4CAF50; color: white; font-size: 14px; padding: 10px; border-radius: 5px;"
        )
        applications_button.clicked.connect(self.open_applications_window)

        # Add buttons to layout
        button_layout.addWidget(cpu_battery_button)
        button_layout.addWidget(graph_button)
        button_layout.addWidget(applications_button)

        layout.addLayout(button_layout)

        # Footer
        footer = QLabel("© 2025 Smart Power Manager. All rights reserved.")
        footer.setStyleSheet("font-size: 12px; color: gray; margin: 10px;")
        footer.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer)

        # Set Layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_cpu_battery_window(self):
        self.cpu_battery_window = CPUBatteryWindow()
        self.cpu_battery_window.setWindowTitle("Smart Power Manager - CPU & Battery Stats")
        self.cpu_battery_window.show()

    def open_graph_window(self):
        self.graph_window = GraphWindow()
        self.graph_window.setWindowTitle("Smart Power Manager - Graphs")
        self.graph_window.show()

    def open_applications_window(self):
        self.applications_window = ApplicationsWindow()
        self.applications_window.setWindowTitle("Smart Power Manager - Running Applications")
        self.applications_window.show()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
