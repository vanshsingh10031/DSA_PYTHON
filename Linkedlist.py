class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at End
    def insert_atEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        print("temp", self.head.data)
        print("Next Value", self.head.next)
        print("Whole Value", self)

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        print("temp Data", temp.next.data)
        print("Next Value", temp.next.next)
        print("Whole Value", temp.next)

    # Display List
    def display(self):
        temp = self.head

        if temp is None:
            print("List is Empty")
            return

        while temp:
            if temp.next:
                print(temp.data, end=" -> ")
            else:
                print(temp.data, end="")
            temp = temp.next
        print()


# Main Program
ll = LinkedList()

while True:
    print("\n----- Linked List Menu -----")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Display List")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        ll.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        ll.insert_atEnd(data)

    elif choice == 3:
        ll.display()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")