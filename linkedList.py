class Node:
    def __init__(self, data, next = None):
        self.data = data      
        self.next_node = next        

class TwoWayNode(Node):
    def __init__(self, data, previous=None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous
        self.size = 0

    def length(self):
        return self.size

    def insert(self, item, index):
        pass
        #if index >= self.size:
    
    def pop(self, index):
        pass

    def makeTwoWay(self):
        pass
    
