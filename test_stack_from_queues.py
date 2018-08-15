from PracticeAlgos.stack_two_queues import StackQueues

def main():
    stack = StackQueues()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.print()
    stack.pop()
    stack.print()
    stack.pop()
    stack.print()
    stack.pop()

if __name__ == "__main__":
    main()