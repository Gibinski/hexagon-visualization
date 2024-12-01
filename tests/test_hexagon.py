import pytest
import numpy as np 
from hexagon_visualization import hexagon

def test_hexagon_vertices():
    """Test that the hexagon function generates the correct number of vertices."""
    center = (0, 0)
    radius = 1
    x, y = hexagon(center, radius)
    assert len(x) == 7, "Hexagon should have 7 vertices (including closure)."
    assert len(y) == 7, "Hexagon should have 7 vertices (including closure)."

def test_hexagon_coordinates():
    """Test that the hexagon function returns correct coordinates for known input."""
    center = (0, 0)
    radius = 1
    x, y = hexagon(center, radius)
    expected_x = [1, 0.5, -0.5, -1, -0.5, 0.5, 1]
    expected_y = [0, np.sqrt(3) / 2, np.sqrt(3) / 2, 0, -np.sqrt(3) / 2, -np.sqrt(3) / 2, 0]
    assert pytest.approx(x) == expected_x, "Hexagon X-coordinates are incorrect."
    assert pytest.approx(y) == expected_y, "Hexagon Y-coordinates are incorrect."
