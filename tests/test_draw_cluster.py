import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from hexagon_visualization import draw_cluster
import matplotlib.pyplot as plt

class TestDrawCluster(unittest.TestCase):
    def test_draw_cluster(self):
        # Test that the function runs without errors
        center = (0, 0)
        radius = 1
        color = 'r-'
        
        # Use Matplotlib's figure to capture the plot
        plt.figure()
        draw_cluster(center, radius, color)
        plt.close()  # Close the plot after testing

if __name__ == '__main__':
    unittest.main()
