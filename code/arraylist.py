from doctest import OutputChecker


class MyArrayList(object):
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 10
        self.theData = [None]*self.capacity
    
    def __len__(self):
        return self.size

    def insert(self, index: int, item):
        if not isinstance(index, int):
            raise IndexError(index + " is not an integer.")
        if index < 0 or index > self.size:
            raise IndexError("Index " + str(index) +  " is out of range.")
        if self.size ==  self.capacity:
            self.__reallocate()

        for i in range(self.size -1, index -1, -1):
            temp =  self.theData[i]
            self.theData[i+1] = temp


        self.theData[index] =  item
        self.size += 1

    def append(self, item):
        self.insert(self.size,item)

    def __reallocate(self):
        self.capacity = self.capacity * 2
        newData =  [None] * self.capacity
        for index, item in enumerate(self.theData):
            newData[index] = item
        self.theData = newData

    def remove(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Index " + str(index) +  " is out of range.")

        item = self.theData[index]

        for index in range(index+1,self.size):
            self.theData[index -1] = self.theData[index]

        self.size = self.size - 1
        return item

    """
    def __str__(self): # first attempt
        output =  "["
        for item in self.theData:
            output += str(item) +","
        output = output[:-1] # remove the last comma
        return output + "]"  
    """
    def __str__(self): # second attempt
        output =  "["
        #only include indexes from 0 to size-1
        for item in self.theData[:self.size]:
            output += str(item) +","
        output = output[:-1] # remove the last comma
        return output + "]"
    # obviated by dunder method
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index " + str(index) +  " is out of range.")
        return self.theData[index]
    
    # obviated by dunder method
    def set(self, index, item):
        if index < 0 or index >= self.size:
            raise IndexError("Index " + str(index) +  " is out of range.")
        oldItem = self.theData[index]
        self.theData[index] = item
        return oldItem


    def __getitem__(self, index):
        if index < 0: 
            index =  index % self.size  # yes! 
            # If you're confused, test modulo on 
            # negative numbers in python.
        if index >= self.size:
            raise IndexError("Index " + str(index) +  " is out of range.")       
        return self.theData[index]
    
    def __setitem__(self, index, item):
        if index < 0: 
            index =  index % self.size
        if index >= self.size:
            raise IndexError("Index " + str(index) +  " is out of range.")
        oldItem = self.theData[index]
        self.theData[index] = item
        return oldItem

l =  MyArrayList()
for i in range(12):
    l.append(i)
l.remove(2)
print(l)