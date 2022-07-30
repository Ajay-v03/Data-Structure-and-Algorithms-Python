from collections import deque
import threading 
import time

'''Generating Binary NUmbers'''
class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, val):
        self.buffer.appendleft(val)  #appendleft add value in left or start or zero index in deque
                                    #appendright add value in end or end or -1 index in deque
        
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]


def generate_binary_numbers(num):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(num):
        front  = numbers_queue.front()
        print('Front: ',front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == '__main__':
    generate_binary_numbers(5)