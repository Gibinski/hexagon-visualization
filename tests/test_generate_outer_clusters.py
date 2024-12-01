import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from hexagon_visualization import generate_outer_clusters
import matplotlib.pyplot as plt

class TestGenerateOuterClusters(unittest.TestCase):
    def test_generate_outer_clusters(self):
        # Test that the function runs without errors
        center = (0, 0)
        radius = 1
        num_clusters = 3
        colors = ['g-', 'y-']
        
        # Use Matplotlib's figure to capture the plot
        plt.figure()
        generate_outer_clusters(center, radius, num_clusters, colors)
        plt.close()  # Close the plot after testing

if __name__ == '__main__':
    unittest.main()
