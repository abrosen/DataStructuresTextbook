from doctest import OutputChecker


class MyArrayList(object):
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 10
        self.theData = [None]*self.capacity
    
    def __len__(self):
        return self.size

    def insert(self, index, item):
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
        self.insert(self,self.size,item)

    def __reallocate(self):
        pass
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


l =  MyArrayList()
l.insert(0, 1)
l.insert(0, 1)
l.insert(0, 1)
l.insert(0, 1)
l.insert(0, 2)
l.insert(0, 2)
l.insert(0, 2)
l.insert(0, 2)
#l.insert(0, 2)
l.insert(0, 2)
print(l)