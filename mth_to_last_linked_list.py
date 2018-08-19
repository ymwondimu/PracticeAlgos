from DataStructures.DoublyLinkedList import DoublyLinkedList

def mth_to_last(n, ll):
    if ll.head == None:
        raise ValueError("Empty LinkedList")
    else:
        count = 0
        curr = ll.head
        trail = None
        while (curr):
            #print (count,n)
            if count == n:
                trail = ll.head
                break
            else:
                curr = curr.next
                count += 1

        if trail == None:
            raise ValueError("Invalid Index")
        else:
            while (curr.next):
                curr = curr.next
                trail = trail.next

        return trail

