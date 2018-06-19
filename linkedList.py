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

    def insert(self, new_item, index):
        head = self
        while index > 0:
            if head.next != None:
                head = head.next
                index -= 1
            else:
                raise IndexError
            head.next = Node(new_item, head.next)

    def pop(self, index):
        pass

    def makeTwoWay(self):
        pass
