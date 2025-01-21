**CHORD System Simulation**

This project simulates a basic CHORD Distributed Hash Table (DHT) system using Python. The CHORD system allows the addition and deletion of nodes and performs lookups to determine which node is responsible for a given key. This project includes a visualization of the CHORD ring using matplotlib, including a step-by-step demonstration of how lookups progress through the system.

**Features**

- **Node Addition**: Adds a new node with a unique ID to the CHORD ring at a random position.
- **Node Deletion**: Randomly removes an existing node from the CHORD ring.
- **Visualization**: Displays the CHORD ring using a circular visualization with nodes positioned according to their IDs.
- **Lookup**: Finds the node responsible for a given key and visually shows the progression of the lookup through the ring.

**Project Structure**

- chord.py: Main program file containing the logic for managing nodes, performing lookups, and user interactions.
- node.py: Defines the Node class, representing a node in the CHORD ring.
- visualization.py: Contains functions for visualizing the CHORD ring and the lookup progression using matplotlib.

**Prerequisites**

- Python 3.x
- matplotlib library for visualization

**How to Run**

1. **Clone the repository** or download the files into a local directory.
1. **Navigate to the project directory**:
1. **Run:** python3 chord.py
1. **Interact with the Menu**:
   1. 1: Add a new node to the CHORD ring.
   1. 2: Delete a random node from the CHORD ring.
   1. 3: Visualize the current state of the CHORD ring.
   1. 4: Perform a lookup for a key and see the visual progression.
   1. 5: Exit the program
