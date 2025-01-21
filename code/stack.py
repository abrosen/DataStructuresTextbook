class Stack:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def peek(self):
        return self.top.item

    def pop(self):
        toReturn = self.top.item
        self.top = self.top.next
        return toReturn

    def push(self, item):
        newTop = self.Node(item)
        newTop.next = self.top
        self.top = newTop
        return item


if __name__ == "__main__":
    s = Stack()
    for i in range(1, 11):
        s.push(i)

    while not s.is_empty():
        print(s.pop())
