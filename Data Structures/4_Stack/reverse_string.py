from collections import deque
from pickletools import StackObject

from numpy import size

class Stack():
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def reverse_string(string_):
    stack = Stack()

    for character in string_:
        stack.push(character)

    rev_str = ''
    while stack.size()!=0:
        rev_str += stack.pop()

    return rev_str

if __name__ == "__main__":
    print(reverse_string('I am player!'))