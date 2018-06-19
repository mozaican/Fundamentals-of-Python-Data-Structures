class Node:
    def __init__(self, data, next = None):
        self.data = data      
        self.next_node = next        

class LinkedList:
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def length(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
    
