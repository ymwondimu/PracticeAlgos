from PracticeAlgos.LinkedList import LinkedList
from PracticeAlgos.stack_with_linked_list import StackLinkedList
def main():
    stack = StackLinkedList()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.print()
    stack.pop()
    stack.print()
    stack.push(100)
    stack.print()

if __name__ == "__main__":
    main()