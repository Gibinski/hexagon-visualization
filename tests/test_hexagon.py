
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from hexagon_visualization import hexagon

class TestHexagonFunction(unittest.TestCase):
    def test_hexagon_vertices(self):
        # Test that the hexagon vertices are correctly calculated
        center = (0, 0)
        radius = 1
        x, y = hexagon(center, radius)
        self.assertEqual(len(x), 7)  # Hexagon should have 6 vertices + 1 (closing)
        self.assertEqual(len(y), 7)
        self.assertAlmostEqual(x[0], x[-1])  # First and last vertices must match
        self.assertAlmostEqual(y[0], y[-1])

    def test_hexagon_non_zero_center(self):
        # Test hexagon with non-zero center
        center = (2, 3)
        radius = 1
        x, y = hexagon(center, radius)
        self.assertAlmostEqual(x[0], center[0] + radius)

if __name__ == '__main__':
    unittest.main()
