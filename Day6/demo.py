class Node:
    def __init__(self, data):
        self.data = data #(5)(10)(20)
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def addNode(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
            


object =LinkedList()
object.addNode(5)
object.addNode(10)
object.addNode(20)
       