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
    def __init__(self, elements=None):
        if elements:
            self.head = Node(elements[0])
            # next item to link with
            next_item = self.head
            for i in range(1, len(elements)):
                next_item.next = Node(elements[i])
                next_item = next_item.next
        else:
            self.head = None
        # for item, index in enumerate(list):
        #     item = Node(item)
        # for item, index in enumerate(list.reverse):
        #     if index == len(list.reverse):
        #         self.head = list[0]
        #     else:
        #         if index != 0:
        #             item.next = list.reverse[index-1]

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
        if self.head:
            next_item = self.head
            while(next_item.next):
                next_item = next_item.next
            next_item.next=node
        else:
            self.head = node


    # Method to add a new node after an existing element
    def add_after(self, target_node_data, new_node):
        next_item = self.head
        while (next_item.next.data != target_node_data) and (next_item.next.next.data != target_node_data):
            next_item = next_item.next
        new_node.next = next_item.next.next
        next_item.next.next = new_node

    # Method to remove a node from the linked list
    def remove_node(self, target_node_data):
        next_item = self.head
        while (next_item.next.data != target_node_data) and (next_item.next.next.data != target_node_data):
            next_item = next_item.next
        next_item.next = next_item.next.next



