# Class for each individual node within the binary tree
# you do not need to change this class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, data):
        # if self.value:
        if data < self.value:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.value:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        # else:
        #     self.value = data

    def find(self, val):
        if val < self.value:
            if self.left == None:
                return None
            else:
                return self.left.find(val)
        elif val > self.value:
            if self.right == None:
                return None
            else:
                return self.right.find(val)
        elif val == self.value:
            return self
        else:
            return None

class Tree:

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add_node(self, node):
        if self.root:
            self.root.insert(node)
        else:
            self.root = Node(node)
        # node = Node(node)
        # if self.root:
        #     if node.value < self.root.value:
        #         if self.root.left == None:
        #             self.root = node
        #         else:
        #             self.add_node(node)
        #     elif node.value > self.root.value:
        #         if self.root.right == None:
        #             self.root = node
        #         else:
        #             self.add_node(node)
        # else:
        #     self.root = node

    def find_node(self, value):
        return self.root.find(value)
        # if self.root:
        #     if value < self.root.value:
        #         if self.root.left == None:
        #             return False
        #         else:
        #             self.find_node(value)
        #     elif value == self.root.value:
        #         return 