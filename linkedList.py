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

    def insert(self, data, index):
        head = TwoWayNode(Node)
        if head is None and index <= 0:
            head = Node(data, head)
        else:
            while index > 1 and head.next != None:
                head = head.next
                index -= 1
            head.next = Node(data, head.next)

    def pop(self, index):
        pass

    def makeTwoWay(self):
        pass
    
if __name__ == "__main__":
    n = TwoWayNode(1)
    n.insert(2,1)
    n.insert(3,2)
    n.insert(4,3)
    print(n.length())