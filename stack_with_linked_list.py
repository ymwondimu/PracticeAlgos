from PracticeAlgos.LinkedList import LinkedList

class StackLinkedList:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, val):
        self.ll.insertAtHead(val)

    def pop(self):
        if self.ll.head == None:
            raise ValueError("Trying to pop from an empty stack.")
        else:
            if self.ll.head.next == None:
                val = self.ll.head
                self.ll.head = None
                return val
            else:
                val = self.ll.head
                self.ll.head = val.next
                return val

    def print(self):
        self.ll.print()