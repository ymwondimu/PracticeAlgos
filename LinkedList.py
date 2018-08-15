from PracticeAlgos.LinkedListNode import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtHead(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            n = Node(val)
            n.next = self.head
            self.head = n

    def insert(self, val):
        if self.head == None:
            n = Node(val)
            self.head = n
            self.size += 1
        else:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = Node(val)
            self.size += 1

    def search(self, val):
        if self.head == None:
            raise ValueError("Empty LinkedList, your value is not found.")
        curr = self.head
        while (curr):
            if curr.val == val:
                return curr
            curr = curr.next
        raise ValueError("Your value was not found in the list")

    def delete(self, val):
        if self.head == None:
            raise ValueError("Attempting to delete from an empty LinkedList")
        if self.head.next == None:
            if self.head.val == val:
                self.head = None
                self.size -= 1
        else:
            prev = self.head
            curr = self.head.next

            if prev.val == val:
                self.head = curr
                prev.next = None
                self.size -= 1
            else:
                while (curr):
                    if curr.val == val:
                        prev.next = curr.next
                        curr.next = None
                        self.size -= 1
                        break
                    curr = curr.next
                    prev = prev.next

    def print(self):
        s = ""
        curr = self.head
        while(curr):
            s+=str(curr.val)+"->"
            #print (curr.val)
            curr = curr.next

        s += "NULL"

        print (s)
