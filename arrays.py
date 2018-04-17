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
