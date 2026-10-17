
import csv
from pathlib import Path
from statistics import mean

SAFE_MIN_CM = 50.0
WARNING_MIN_CM = 20.0
MAX_DISTANCE_CM = 400.0


def validate_reading(value):
    """Check whether a distance reading is valid."""
    if isinstance(value, bool):
        return False

    try:
        distance = float(value)
    except (TypeError, ValueError):
        return False

    return 0 < distance <= MAX_DISTANCE_CM


def classify_distance(distance_cm):
    """Classify one valid distance reading."""
    if not validate_reading(distance_cm):
        raise ValueError("Invalid distance reading")

    distance_cm = float(distance_cm)

    if distance_cm >= SAFE_MIN_CM:
        return "SAFE"
    elif distance_cm >= WARNING_MIN_CM:
        return "WARNING"
    return "DANGER"


def analyze_readings(readings):
    """Validate readings and calculate summary statistics."""
    valid = []
    invalid_count = 0

    for value in readings:
        if validate_reading(value):
            valid.append(float(value))
        else:
            invalid_count += 1

    if not valid:
        raise ValueError("No valid readings available")

    states = [classify_distance(value) for value in valid]

    summary = {
        "count": len(valid),
        "invalid_count": invalid_count,
        "minimum_cm": min(valid),
        "mean_cm": mean(valid),
        "maximum_cm": max(valid),
        "states": states,
    }

    return valid, summary


def save_csv(readings, output_path):
    """Save valid readings and their classifications."""
    valid, summary = analyze_readings(readings)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["reading_number", "distance_cm", "state"])

        for index, distance in enumerate(valid, start=1):
            writer.writerow([
                index,
                distance,
                classify_distance(distance)
            ])


if __name__ == "__main__":
    simulated_readings = [
        120, 95, 72, 55, 48, 35, 22, 18, 12, 60,
        0, -5, "bad-data", 410
    ]

    valid, result = analyze_readings(simulated_readings)

    print("Valid readings:", result["count"])
    print("Invalid readings:", result["invalid_count"])
    print("Minimum:", result["minimum_cm"], "cm")
    print("Mean:", round(result["mean_cm"], 2), "cm")

    for distance, state in zip(valid, result["states"]):
        print(f"{distance:7.2f} cm -> {state}")

    save_csv(
        simulated_readings,
        "output/readings.csv"
    )

    print("CSV saved successfully.")
