import matplotlib.pyplot as plt

def plot_energy_usage(data):
    times = [entry['time'] for entry in data]
    usages = [entry['usage'] for entry in data]

    plt.plot(times, usages, label="Energy Usage")
    plt.xlabel("Time")
    plt.ylabel("Energy Usage (%)")
    plt.title("Energy Usage Over Time")
    plt.legend()
    plt.show()