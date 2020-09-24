
class Stack():
    # my_stack = Stack(10)
    def __init__(self, size):
        self.size = size
        self.top_of_stack = -1
        self.storage = [""] * size

    # add new data to the stack - my_stack.push("FOO")
    def push(self, new_element):
        # if self.top_of_stack <=  self.size-1:
        self.storage[self.top_of_stack+1] = new_element
        self.top_of_stack += 1

    # remove and return the top of the stack - my_stack.pop()
    def pop(self):
        # if self.top_of_stack != -1:
        popped = self.storage[self.top_of_stack]
        # self.storage[self.top_of_stack+1] = ''
        self.top_of_stack -= 1
        return popped

    # looking at the top of the stack, but don't change anything! - my_stack.peek()
    def peek(self):
        return self.storage[self.top_of_stack]

