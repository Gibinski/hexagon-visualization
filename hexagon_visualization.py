# Re-importing necessary libraries after environment reset
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate hexagon vertices
def hexagon(center, radius):
    """Calculate the vertices of a hexagon based on its center and radius."""
    angles = np.linspace(0, 2 * np.pi, 7)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y

# Function to plot a hexagon cluster (central and surrounding hexagons)
def seven_hex(main_center, main_radius, color, offsets):
    """
    Draw a central hexagon and its surrounding six hexagons.
    :param main_center: Tuple for the central hexagon's center.
    :param main_radius: Radius of the hexagons.
    :param color: Color of the outer hexagons.
    :param offsets: List of offsets for surrounding hexagons.
    """
    # Draw central hexagon
    main_x, main_y = hexagon(main_center, main_radius)
    plt.plot(main_x, main_y, 'b-', label='Central Hexagon')

    # Draw surrounding hexagons
    for offset in offsets:
        outer_center = (main_center[0] + offset[0], main_center[1] + offset[1])
        outer_x, outer_y = hexagon(outer_center, main_radius)
        plt.plot(outer_x, outer_y, color)

# Parameters
main_radius = 1  # Radius of the hexagons

# Offsets for surrounding hexagons in a seven-hex cluster
offsets = [
    (0, 2 * main_radius),  # Top
    (np.sqrt(3) * main_radius, main_radius),  # Top-right
    (np.sqrt(3) * main_radius, -main_radius),  # Bottom-right
    (0, -2 * main_radius),  # Bottom
    (-np.sqrt(3) * main_radius, -main_radius),  # Bottom-left
    (-np.sqrt(3) * main_radius, main_radius),  # Top-left
]

# Offsets for positioning clusters of seven hexagons
offsets_hex = [
    (np.sqrt(3), 5),
    (np.sqrt(3) * 3, 1),
    (np.sqrt(3) * 2, -4),
    (-np.sqrt(3), -5),
    (-np.sqrt(3) * 3, -1),
    (-np.sqrt(3) * 2, 4),
]

# Colors for alternating clusters
colors = ["g-", "y-"]

# Plotting
plt.figure(figsize=(10, 10))
seven_hex((0, 0), main_radius, "r-", offsets)  # Central cluster in red
for idx, offset in enumerate(offsets_hex):
    cluster_center = offset
    seven_hex(cluster_center, main_radius, colors[idx % 2], offsets)  # Alternating colors for clusters

# Formatting
plt.gca().set_aspect('equal')
plt.title("Hexagon with Outer Hexagon Clusters")
plt.grid(True)
plt.show()
