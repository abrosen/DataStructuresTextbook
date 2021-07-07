class LinkedList(object):
    
    class Node(object):
        def __init__(self, item) -> None:
            self.item = item
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def add(self, index, item):
        if(index < 0 or index > self.size):
            raise Exception("Invalid add at index " + str(index) +" with item" + str(item) +".")
        
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

    def getNode(self,index):
        current = self.head
        for i in range(index):
            current = current.next
        return current

l = LinkedList()
print(len(l))