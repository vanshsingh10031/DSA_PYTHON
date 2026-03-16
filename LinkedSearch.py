class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    
    def search(self, key):

        temp = self.head
        
        if temp.head == None:
            print("List is Empty")
            return

        while temp is not None:
            if temp.data == key:
                print("Found")
                return
            temp = temp.next    

        print("Not Found")

    # Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete at End
    def Delete_atEnd(self):
        #checking if list is empty
        if self.head is None:
            print("List is Empty")
            return

        # Checking if list has only one node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        # Traverse to second last node
        while temp.next.next:
            temp = temp.next

        # Remove last node
        temp.next = None

    # Insert at End
    def insert_atEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

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
    print("4. Delete At End")
    print("6. Search for an Element")
    print("5. Exit")

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
        ll.Delete_atEnd()

    elif choice == 6:
        data = int(input("Enter element to search: "))
        ll.search(data)

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")