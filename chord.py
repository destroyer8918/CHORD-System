import random
from node import Node
from visualization import visualize_chord  # Ensure visualization.py is in the same directory

class ChordSystem:
    def __init__(self):
        self.nodes = []
        self.start_node()

    def start_node(self):
        # Initialize with a single node
        new_node = Node(random.randint(0, 255))  # Using 0-255 as example ID range
        self.nodes.append(new_node)
        print(f"Starting CHORD system with Node {new_node.id}")

    def add_node(self):
        new_id = random.randint(0, 255)
        while any(node.id == new_id for node in self.nodes):
            new_id = random.randint(0, 255)
        new_node = Node(new_id)
        self.nodes.append(new_node)
        self.nodes.sort(key=lambda x: x.id)
        print(f"Added Node {new_node.id}")

    def delete_node(self):
        if not self.nodes:
            print("No nodes to delete!")
            return
        delete_id = random.choice(self.nodes).id
        self.nodes = [node for node in self.nodes if node.id != delete_id]
        print(f"Deleted Node {delete_id}")

    def visualize(self):
        if len(self.nodes) == 0:
            print("No nodes to visualize.")
        else:
            visualize_chord(self.nodes)

    def lookup(self, key):
        if not self.nodes:
            print("No nodes in the CHORD system!")
            return
        
        print(f"Looking up key {key}...")
        visited_nodes = []
        sorted_nodes = sorted(self.nodes, key=lambda x: x.id)

        # Find the first node whose ID is >= key
        for node in sorted_nodes:
            visited_nodes.append(node)
            if node.id >= key:
                print(f"Key {key} is found at Node {node.id}")
                self.visualize_lookup_progress(visited_nodes, key, node.id)
                return

        # If key is greater than any node's ID, it wraps around to the first node
        print(f"Key {key} is found at Node {sorted_nodes[0].id}")
        visited_nodes.append(sorted_nodes[0])
        self.visualize_lookup_progress(visited_nodes, key, sorted_nodes[0].id)

    def visualize_lookup_progress(self, visited_nodes, key, final_node_id):
        # Call the visualization with special highlighting for visited nodes and the final node
        visualize_chord(self.nodes, visited_nodes, final_node_id, key)

    def user_menu(self):
        while True:
            print("\n1. Add Node\n2. Delete Node\n3. Visualize CHORD\n4. Lookup Key\n5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_node()
            elif choice == '2':
                self.delete_node()
            elif choice == '3':
                self.visualize()
            elif choice == '4':
                key = int(input("Enter the key to lookup: "))
                self.lookup(key)
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    chord_system = ChordSystem()
    chord_system.user_menu()
