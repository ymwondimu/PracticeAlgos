from collections import deque

class StackQueues:
    def __init__(self):
        self.q_in = deque()
        self.q_out = deque()

    def push(self, val):
        self.q_in.append(val)

    def pop(self):
        n = len(self.q_in)
        while (n > 1):
            self.q_out.append(self.q_in.popleft())
            n-=1
        res = self.q_in.popleft()

        n2 = len(self.q_out)
        while (n2 > 0):
            self.q_in.append(self.q_out.popleft())
            n2-=1

        return res

    def print(self):
        print (self.q_in)