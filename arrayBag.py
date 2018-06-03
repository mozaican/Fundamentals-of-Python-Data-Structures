"""
Interface for a collection of items stored in a type of
object like an array bag.   
"""
from arrays import Array

class ArrayBag():

    DEFAULT_CAPACITY = 10

    #constructor
    def __init__(self, sourceCollection = None):
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    #accessor methods
    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self.size

    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result
    
    def __eq__(self, other):
        if self in other: 
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if not item in other: 
                return False
        return True

    #mutator methods
    def clear(self):
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
    
    def add(self, item):
        self.items[len(self)] = item
        self.size += 1

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        for i in range(targetIndex, len(self) - 1):
            self.items[i] = self.items[i + 1]
        self.size -= 1
