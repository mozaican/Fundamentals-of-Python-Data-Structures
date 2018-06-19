class Node:
    def __init__(self, data, next = None):
        self.data = data      
        self.next = next        

class TwoWayNode(Node):
    def __init__(self, data, previous=None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous

    def length(self):
        temp = self.next
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def insert(self, item, index):
        pass
        #if index >= self.size:
    
    def pop(self, index):
        pass

    def makeTwoWay(self):
        pass
    
