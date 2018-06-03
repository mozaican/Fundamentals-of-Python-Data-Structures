class Array:
    def __init__(self, capacity, fillValue = None):
        self.items = list()
        self.logicalSize = 0
        self.fillValue = fillValue
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        return len(self.items)     

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, newItem):
        self.items[index] = newItem
        
        if newItem != self.fillValue:
            self.logicalSize += 1

    def size(self):
        return self.logicalSize

    def grow(self, newItem):
        if self.logicalSize == len(self.items):
            temp = self.__class__(len(self.items) + 1)
            for i in range(len(self.items)):   
                temp.items[i] = self.items[i] 
            self.items = temp.items
            self.__setitem__(len(self.items) - 1, newItem)


    def shrink(self):
        pass

if __name__ == '__main__':
    a = Array(5)
    for i in range(len(a)):
        a[i] = i + 1
    print(a)  
    a.grow(5)
    print(a) 