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
        if elements is None:
            self.head = None
        else:
            self.head = Node(elements[0])
            cur = self.head
            for i in range(1, len(elements)):
                cur.next = Node(elements[i])
                cur = cur.next

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
        if self.head is None:
            self.head = node
        else:
            self.add_to_end_helper(self.head, node)

    def add_to_end_helper(self, cur, node):
        if cur.next is None:
            cur.next = node
        else:
            self.add_to_end_helper(cur.next, node)

    # Method to add a new node after an existing element
    def add_after(self, target_node_data, new_node):
        cur = self.head
        not_found = True
        while not_found:
            if cur.data == target_node_data:
                not_found = False
            else:
                cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

    # Method to remove a node from the linked list
    def remove_node(self, target_node_data):
        if self.head is None:
            return
        elif self.head.data == target_node_data:
            self.head = self.head.next
        else:
            self.remove_helper(self.head.next, self.head, target_node_data)

    def remove_helper(self, cur, before, target):
        if cur is None:
            return
        elif cur.data == target:
            before.next = cur.next
        else:
            self.remove_helper(cur.next, cur, target)


