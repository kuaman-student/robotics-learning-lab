
import random
from pathlib import Path

import matplotlib.pyplot as plt
import os


def generate_readings(count=50, seed=42, add_outlier=True):
    random.seed(seed)

    times = []
    distances = []

    for index in range(count):
        time_s = index * 0.1

        # Simulate an object gradually approaching.
        true_distance = 120 - 1.5 * index

        # Add small random measurement noise.
        noise = random.uniform(-3, 3)
        measured_distance = true_distance + noise

        # Add one deliberately unusual reading.
        if add_outlier and index == 25:
            measured_distance += 45

        times.append(time_s)
        distances.append(measured_distance)

    return times, distances


if __name__ == "__main__":
    times, distances = generate_readings()


    plt.plot(times, distances, marker=".", label="Measured distance")
    plt.axhline(50, linestyle="--", label="SAFE threshold")
    plt.axhline(20, linestyle="--", label="WARNING threshold")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Distance (cm)")
    plt.title("Simulated Sensor Readings")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    os.makedirs("output", exist_ok=True)  
    plt.savefig("output/readings.png")
    plt.show()
