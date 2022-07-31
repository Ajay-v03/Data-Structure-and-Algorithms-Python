from collections import deque

from soupsieve import match

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

def is_match(ch1, ch2):
    match_dict = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    return match_dict[ch1] == ch2

def is_balanced(string_):
    stack = Stack()

    for character in string_:
        if character =='(' or character == '[' or character == '{':
            stack.push(character)
        if character == ')' or character == ']' or character =='}':
            if stack.size() == 0:
                return False
            if not is_match(character,stack.pop()):
                return False

    return stack.size() == 0


if __name__ == '__main__':
    # print(is_balanced("({a+b})"))
    # print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))