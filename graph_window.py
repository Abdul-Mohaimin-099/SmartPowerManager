from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import QTimer
from collections import deque
from datetime import datetime, timedelta
from resource_monitor import get_cpu_usage, get_battery_status


class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Power Manager - Graphs")
        self.setGeometry(100, 100, 800, 600)

        # Initialize data storage for 1 hours ( 60 * 60 = 3600 seconds)
        self.time_data = deque(maxlen=3600)  # Time points
        self.cpu_data = deque(maxlen=3600)  # CPU usage percentage
        self.battery_data = deque(maxlen=3600)  # Battery percentage

        self.init_ui()

        # Timer to update the graphs
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(1000)  # Update every second

    def init_ui(self):
        layout = QVBoxLayout()

        # Matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        layout.addWidget(self.canvas)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    def update_graph(self):
        # Fetch current CPU and battery stats
        cpu = get_cpu_usage()
        battery = get_battery_status()["percent"]
        # Get the current time
        current_time = datetime.now()
        # Append the new data to the deques
        self.time_data.append(current_time)
        self.cpu_data.append(cpu)
        self.battery_data.append(battery)
        # Clear the figure and plot updated data
        self.figure.clear()
        # Plot CPU Usage
        ax1 = self.figure.add_subplot(2, 1, 1)
        ax1.plot(self.time_data, self.cpu_data, label="CPU Usage (%)", color="red")
        ax1.set_title("CPU Usage Over Last 1 Hour")
        ax1.set_ylabel("CPU Usage (%)")
        ax1.set_xlim([current_time - timedelta(hours=1), current_time])  # Show last 1 hour
        ax1.grid(True)
        ax1.legend()
        # Plot Battery Percentage
        ax2 = self.figure.add_subplot(2, 1, 2)
        ax2.plot(self.time_data, self.battery_data, label="Battery Percentage (%)", color="blue")
        ax2.set_title("Battery Percentage Over Last 1 Hour")
        ax2.set_ylabel("Battery Percentage (%)")
        ax2.set_xlim([current_time - timedelta(hours=1), current_time])  # Show last 1 hour
        ax2.set_xlabel("Time")
        ax2.grid(True)
        ax2.legend()
        # Redraw the canvas
        self.canvas.draw()
