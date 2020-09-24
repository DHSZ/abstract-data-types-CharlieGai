class Queue():
    def __init__(self, size):
        self.size = size
        self.front_index = 0
        self.end_index = -1
        self.storage = [""] * size

    # add new data to the end of the queue
    def enqueue(self, new_element):

        self.end_index += 1
        if self.end_index < self.size:
            self.storage[self.end_index] = new_element
        else:
            self.end_index -= self.size
            self.storage[self.end_index-self.size] = new_element

    # remove data from the front of the queue
    def dequeue(self):
        dequeued = self.storage[self.front_index]
        self.storage[self.front_index] = None
        self.front_index += 1
        return dequeued
