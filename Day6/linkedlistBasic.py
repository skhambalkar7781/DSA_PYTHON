class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

LinkedList = LinkedList()
LinkedList.head = Node(5)
second = Node(10)
third = Node(15)
fouth = Node(20)

#connecting nodes
LinkedList.head.next = second
second.next = third
third.next = fouth

#display linked list

while LinkedList.head != None:
    print(LinkedList.head.data,"!",LinkedList.head.next,"->" ,end="")
    LinkedList.head = LinkedList.head.next
    
    