
import unittest
import os
import sys

# Adds the 'tasks' directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Task04.analyzer import (
    validate_reading,
    classify_distance,
    analyze_readings,
)


class TestDistanceAnalyzer(unittest.TestCase):

    def test_valid_readings(self):
        self.assertTrue(validate_reading(35))
        self.assertTrue(validate_reading("35.5"))
        self.assertTrue(validate_reading(400))

    def test_invalid_readings(self):
        self.assertFalse(validate_reading(0))
        self.assertFalse(validate_reading(-1))
        self.assertFalse(validate_reading(400.1))
        self.assertFalse(validate_reading("bad-data"))
        self.assertFalse(validate_reading(True))

    def test_boundaries(self):
        self.assertEqual(classify_distance(19.9), "DANGER")
        self.assertEqual(classify_distance(20), "WARNING")
        self.assertEqual(classify_distance(49.9), "WARNING")
        self.assertEqual(classify_distance(50), "SAFE")

    def test_invalid_classification_raises_error(self):
        with self.assertRaises(ValueError):
            classify_distance(-1)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            analyze_readings([])

    def test_all_invalid_input(self):
        with self.assertRaises(ValueError):
            analyze_readings([0, -1, "bad-data", 401])

    def test_statistics(self):
        _, summary = analyze_readings([10, 20, 30])

        self.assertEqual(summary["minimum_cm"], 10)
        self.assertEqual(summary["mean_cm"], 20)
        self.assertEqual(summary["count"], 3)


if __name__ == "__main__":
    unittest.main()
