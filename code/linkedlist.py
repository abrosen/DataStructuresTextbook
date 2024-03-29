from typing import Generic, TypeVar


E =  TypeVar('E')

class LinkedList(Generic[E]):

    class Node(Generic[E]):
        def __init__(self, item: E) -> None:
            self.item = item
            self.next = None

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self) -> int: 
        return self.size

    def getNode(self, index: int) -> Node:
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def add(self, item: E) -> bool:
        self.add(self.size,item)
        return True

    def add(self, index: int, item: E) -> None:
        if(index < 0 or index > self.size):
            raise IndexError("Invalid add at index " + str(index) +" with item" + str(item) +".")
        
        adding = self.Node(item)
        if(self.size == 0):
            self.head = adding
            self.tail = adding
        elif(index == 0):
            adding.next = self.head
            self.head = adding
        elif(index == self.size):
            self.tail.next = adding
            self.tail = adding
        else:
            before = self.getNode(index - 1)
            adding.next = before.next
            before.next = adding

        self.size += 1

    def remove(self, index: int) -> E:
        if(index < 0 or index >= self.size):
            raise Exception("Invalid remove at index " + str(index) +".")
        
        toReturn = None
        if self.size == 1:
            toReturn =  self.head.item
            self.head = None
            self.tail = None
        elif index == 0:
            toReturn = self.head.item
            self.head = self.head.next
        elif index == self.size -1:
            toReturn = self.tail.item
            self.tail = self.getNode(index - 1)
            self.tail.next =  None
        else:
            before =  self.getNode(index - 1)
            toReturn = before.next.item
            before.next = before.next.next
        self.size -= 1
        return toReturn

    def get(self, index: int) -> E:
        return self.getNode(index).item

    def set(self, index: int, item: E) -> E:
        node = self.getNode(index)
        oldItem = node.item
        node.item = item
        return oldItem

    def __str__(self) -> str:
        output = ""
        current = self.head
        while current != None:
            output += str(current.item) + "->"
            current = current.next
        return output[:-2]


l = LinkedList()
l.add(3)
l.add(5)
l.add(142)