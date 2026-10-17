def classify_distance(distance_cm):
    if distance_cm >= 50:
        return "SAFE"
    elif distance_cm >= 20:
        return "WARNING"
    else:
        return "DANGER"

print(classify_distance(80))
print(classify_distance(35))
print(classify_distance(10))

readings = [80, 72, 45, 18, 12, 55]

for distance in readings:
    state = classify_distance(distance)
    print(distance, "cm ->", state)


class RobotPose:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

pose = RobotPose(1.0, 2.0, 0.5)

print(pose.x)
print(pose.y)
print(pose.theta)


with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("First robotics note\n")



raw_value = "not-a-number"

try:
    distance_cm = float(raw_value)
except ValueError:
    print("Invalid numeric reading")



import logging

logging.basicConfig(level=logging.INFO)

logging.info("Analyzer started")
logging.warning("Distance is below warning threshold")
logging.error("Could not read sensor data")



import numpy as np

readings = np.array([10, 20, 30, 40])

print(readings.mean())
print(readings.min())
print(readings.max())