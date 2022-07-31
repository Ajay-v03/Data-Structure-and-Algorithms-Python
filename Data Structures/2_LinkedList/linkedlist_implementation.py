from tkinter import N
from tkinter.messagebox import NO


class Node: #Node always took data and next element ref
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList: #LinkedList is a collection of nodes
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data): #insert element at begining in linkedlist
        node = Node(data,self.head)
        self.head = node

    def print(self): #print all elemsts in linkedlist
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def get_length(self): #get length of a linked list
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_end(self,data): #insert data at end of linked list
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_at(self,index,data): #insert data at given index of linked list
        if index < 0  or index > self.get_length():
            raise Exception ("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return
        
        itr = self.head
        count  = 0
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self,index): #remove data at given index or specified index
        if index < 0  or index > self.get_length():
            raise Exception ("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count  = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1

    def insert_bulk_values(self,data_list): #insert number of values in single operation
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    root = LinkedList()
    # root.insert_at_begining(2)
    # root.insert_at_begining(5)
    # root.insert_at_begining(7)
    # print(root.get_length())
    # root.insert_at_end(232)
    # root.insert_at_end(343)
    # root.insert_at_end(444)
    # root.print()
    # root.insert_at(1,555)
    # root.print()
    # root.remove_at(1)
    # root.print()
    root.insert_at_end(['Hockey','Cricket','Basketball','Gym','Yoga'])
    root.print()