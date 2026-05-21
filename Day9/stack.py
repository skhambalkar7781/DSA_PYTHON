class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        currentnode = self.head
        while currentnode:
            yield currentnode
            currentnode = currentnode.next
        
class stack:
    def __init__(self):
        self.LinkedList = LinkedList()
        
    def pop(self):
        if self.isEmpty():
            return("Stack is empty")
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return("Stack is empty")
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
    
    def isEmpty(self):
        if self.LinkedList.head== None:
            return True
        else:
            return False
    def __str__(self):
        value = [str(x.value) for x in self.LinkedList]
        return '\n'.join(value)
    
        
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        
customStack = stack()
customStack.push(10)
customStack.push(20)
customStack.push(30)
print(customStack)