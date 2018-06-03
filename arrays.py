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
        try:
            return self.items[index]
        except(TypeError, IndexError):
            print("Index in not correct!")

    def __setitem__(self, index, newItem):
        try:
            self.items[index] = newItem
            if newItem != self.fillValue:
                self.logicalSize += 1
        except(TypeError, IndexError):
            print("Index is not correct!")

    def size(self):
        return self.logicalSize

    def grow(self):
        if self.logicalSize == len(self.items):
            temp = self.__class__(len(self.items) * 2)
            for i in range(len(self.items)):   
                temp.items[i] = self.items[i] 
            self.items = temp.items

    def shrink(self):
        if self.logicalSize <= len(self.items) // 2:
            temp = self.__class__(len(self.items) // 2)
            for i in range(self.logicalSize):
                temp.items[i] = self.items[i]
            self.items = temp.items

if __name__ == '__main__':
    a = Array(5)
    for i in range(len(a)):
        a[i] = i + 1
    print(a)  