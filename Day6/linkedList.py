class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
def addNode(self, value):
    self.head = Node(value)
    if self.head is None:
        self.head = self.head
        self.tail = self.node
    else:
        self.tail.next = self.node
        self.tail = self.node
        
def addNodeInBetween(self, value, index):
    self.node = Node(value)
    if self.head is None:
        self.head = self.node
        self.tail = self.node
    else:
        self.tail.next = self.node
        self.tail = self.node
        
def displaynode(self):
    while self.head is not None:
        print(self.head.data)
        self.head = self.head.next
        
if __name__ == "__main__":
    object = LinkedList()                             
    while True:
        print("1. Add Node LinkedList")
        print("2. Add node in beginning")
        print("3. Add node in between")
        print("4. Add node in end")
        print("5. Display LinkedList")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            value = int(input("Enter the value: "))
            object.addNode(value)
            print("Node added successfully in single linked list")
        elif choice == 5:
            object.displaynode()
            
        elif choice == 3:
            value = int(input("Enter the value: "))
            index = int(input("Enter the index: "))
            object.addNodeInBetween(value, index)
        