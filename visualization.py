import matplotlib.pyplot as plt
import numpy as np

def visualize_chord(nodes, visited_nodes=[], final_node_id=None, key=None):
    # Convert node IDs into angles (0 to 2*pi for a full circle)
    angles = [node.id / 256 * 2 * np.pi for node in nodes]
    visited_angles = [node.id / 256 * 2 * np.pi for node in visited_nodes]
    final_angle = final_node_id / 256 * 2 * np.pi if final_node_id is not None else None
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_yticklabels([])
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title(f"CHORD Ring Visualization - Lookup for Key {key}")

    # Plot each node
    for angle, node in zip(angles, nodes):
        ax.plot([angle, angle], [0, 1], color='gray', marker='o')
        ax.text(angle, 1.05, f"{node.id}", ha='center', va='center')

    # Highlight visited nodes in a different color
    for angle in visited_angles:
        ax.plot([angle, angle], [0, 1], color='blue', marker='o', linewidth=2)

    # Highlight the final responsible node
    if final_angle is not None:
        ax.plot([final_angle, final_angle], [0, 1], color='red', marker='o', linewidth=3, label=f"Responsible Node {final_node_id}")

    # Show legend
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
    plt.show()
