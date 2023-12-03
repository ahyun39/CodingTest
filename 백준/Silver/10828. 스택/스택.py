import sys
input = sys.stdin.readline

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0

    def top(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[-1]

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s = Stack()
    n = int(input())
    for _ in range(n):
        order = input().split()
        if order[0] == 'push':
            s.push(order[1])
        elif order[0] == 'pop':
            print(s.pop())
        elif order[0] == 'size':
            print(s.size())
        elif order[0] == 'empty':
            print(s.is_empty())
        else: # top
            print(s.top())
