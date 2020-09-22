# Class for each individual node within the Linked List
# you do not need to change this class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Class for the list structure itself
class LinkedList:
    # This method will run when you create a new
    # linked list object instance
    def __init__(self):
        self.head = None

    # This method will make a nicely printed version
    # of your linked list structure, don't change it!
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # Method to add a new node to the start of the linked list
    def add_to_start(self, node):
        node.next = self.head
        self.head = node

    # Method to add a new node at the end of the linked list
    def add_to_end(self, node):
        self.data.append(node)

    # Method to add a new node after an existing element
    def add_after(self, target_node_data, new_node):
        pass

    # Method to remove a node from the linked list
    def remove_node(self, target_node_data):
        pass

