class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add node at end
    def addNode(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Add node in between using index
    def addNodeInBetween(self, value, index):
            self.node = Node(value)
            if self.head is None:
                self.head = self.node
                self.tail = self.node
            else:
                temp = self.head
                for _ in range(index-1):
                    temp = temp.next
                self.node.next = temp.next
                temp.next = self.node
                

    # Display linked list
    def displaynode(self):
        temp = self.head

        if temp is None:
            print("Linked List is empty")
            return

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


if __name__ == "__main__":
    obj = LinkedList()

    while True:
        print("\n1. Add Node")
        print("2. Add node in between")
        print("3. Display LinkedList")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the value: "))
            obj.addNode(value)
            print("Node added successfully")

        elif choice == 2:
            value = int(input("Enter the value: "))
            index = int(input("Enter the index: "))
            obj.addNodeInBetween(value, index)
            print("Node inserted successfully")

        elif choice == 3:
            obj.displaynode()

        elif choice == 4:
            print("Program Ended")
            break

        else:
            print("Invalid Choice")