from os import remove
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

    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            
            itr = itr.next

    def remove_by_value(self,data):
        if self.head is None:
            return
        
        if self.head == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_bulk_values(['Hockey','Cricket','Basketball','Gym','Yoga'])
    ll.print()
    ll.insert_after_value('Cricket','Kho-kho')
    ll.print()
    ll.remove_by_value('Basketball')
    ll.print()
    ll.remove_by_value('Yoga')
    ll.print()
    ll.remove_by_value('Gym')
    ll.remove_by_value('Kho-kho')
    ll.remove_by_value('Cricket')
    ll.print()
