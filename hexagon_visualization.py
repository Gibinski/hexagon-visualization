import matplotlib.pyplot as plt
import numpy as np

def hexagon(center, radius):
    """
    Calculate the vertices of a hexagon given its center and radius.
    Args:
        center (tuple): The (x, y) coordinates of the hexagon's center.
        radius (float): The radius of the hexagon.
    Returns:
        tuple: Two lists (x, y) containing the coordinates of the vertices.
    """
    angles = np.linspace(0, 2 * np.pi, 7)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y

def draw_cluster(main_center, radius, color):
    """
    Draw a cluster of 7 hexagons: one central and six surrounding it.
    Args:
        main_center (tuple): The (x, y) coordinates of the central hexagon.
        radius (float): The radius of each hexagon.
        color (str): The color of the surrounding hexagons.
    """
    # Draw the central hexagon
    x, y = hexagon(main_center, radius)
    plt.plot(x, y, 'b-', label="Central Hexagon")

    # Offsets for surrounding hexagons
    offsets = [
        (0, 2 * radius),  # Top
        (np.sqrt(3) * radius, radius),  # Top-right
        (np.sqrt(3) * radius, -radius),  # Bottom-right
        (0, -2 * radius),  # Bottom
        (-np.sqrt(3) * radius, -radius),  # Bottom-left
        (-np.sqrt(3) * radius, radius),  # Top-left
    ]

    # Draw the surrounding hexagons
    for offset in offsets:
        surrounding_center = (main_center[0] + offset[0], main_center[1] + offset[1])
        x, y = hexagon(surrounding_center, radius)
        plt.plot(x, y, color)

def generate_outer_clusters(center, radius, num_clusters, colors):
    """
    Generate and draw outer clusters of hexagons around a central cluster.
    Args:
        center (tuple): The (x, y) coordinates of the central cluster.
        radius (float): The radius of each hexagon.
        num_clusters (int): The number of clusters to draw around the center.
        colors (list): A list of colors to alternate between clusters.
    """
    # Offsets for the outer clusters
    cluster_offsets = [
        (np.sqrt(3), 5),
        (np.sqrt(3) * 3, 1),
        (np.sqrt(3) * 2, -4),
        (-np.sqrt(3), -5),
        (-np.sqrt(3) * 3, -1),
        (-np.sqrt(3) * 2, 4),
    ]

    # Draw each cluster
    for idx, offset in enumerate(cluster_offsets[:num_clusters]):
        cluster_center = (center[0] + offset[0], center[1] + offset[1])
        draw_cluster(cluster_center, radius, colors[idx % len(colors)])

# Main script
if __name__ == "__main__":
    # Parameters
    central_hexagon_center = (0, 0)
    hexagon_radius = 1
    num_outer_clusters = 6  # Number of outer clusters to draw
    cluster_colors = ['g-', 'y-']  # Alternating colors

    # Plotting
    plt.figure(figsize=(10, 10))
    
    # Draw the central cluster
    draw_cluster(central_hexagon_center, hexagon_radius, 'r-')
    
    # Draw outer clusters
    generate_outer_clusters(central_hexagon_center, hexagon_radius, num_outer_clusters, cluster_colors)

    # Formatting
    plt.gca().set_aspect('equal')
    plt.title("Hexagon Clusters (Aligned and Non-Overlapping)")
    plt.grid(True)
    plt.show()
