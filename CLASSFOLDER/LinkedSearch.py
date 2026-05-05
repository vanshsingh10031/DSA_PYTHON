class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.is_circular = False  # Helps with display choice, but not used for correctness

    # ─────────────── Normal (Singly) Linked List Operations ───────────────

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_atEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_atPosition(self, data, position):
        if position < 0:
            print("Position cannot be negative!")
            return

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next

        if temp is None:
            print("Position out of bounds")
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_atEnd(self):
        if self.head is None:
            print("List is Empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def search(self, key):
        if self.head is None:
            print("List is Empty")
            return False

        temp = self.head
        position = 0
        while temp:
            if temp.data == key:
                print(f"Found {key} at position {position}")
                return True
            temp = temp.next
            position += 1

        print(f"{key} → Not Found")
        return False

    def display_normal(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head
        while temp:
            if temp.next:
                print(temp.data, end=" → ")
            else:
                print(temp.data, end="")
            temp = temp.next
        print()

    # ─────────────── Circular Linked List Operations ───────────────

    def insert_atBeginning_Circular(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.is_circular = True
            return

        # Find last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head
        self.head = new_node
        
    def insert_atEnd_Circular(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.is_circular = True
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head
        self.is_circular = True

    def display_circular(self):
        if self.head is None:
            print("Circular List is empty")
            return

        print("Circular Linked List: ", end="")
        temp = self.head
        start = self.head

        while True:
            print(temp.data, end=" → ")
            temp = temp.next
            if temp == start:
                break

        print("(back to head)")

    # Unified display method
    def display(self):
        if self.is_circular:
            self.display_circular()
        else:
            self.display_normal()


# ──────────────────────────────── MAIN MENU ────────────────────────────────
def main():
    ll = LinkedList()

    while True:
        print("\n===== Linked List Operations =====")
        print("1. Insert at Beginning     (normal)")
        print("2. Insert at End           (normal)")
        print("3. Insert at Position      (normal)")
        print("4. Delete at End           (normal)")
        print("5. Search Element")
        print("6. Display List            (auto detects mode)")
        print("-------------------------------")
        print("7. Insert at Beginning     (CIRCULAR)")
        print("8. Insert at End           (CIRCULAR)")
        print("9. Display Circular        (force circular view)")
        print("-------------------------------")
        print("10. Switch mode            (toggle normal ↔ circular)")
        print("11. Exit")

        try:
            choice = int(input("\nEnter choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            data = int(input("Enter data: "))
            ll.insert_beginning(data)

        elif choice == 2:
            data = int(input("Enter data: "))
            ll.insert_atEnd(data)

        elif choice == 3:
            try:
                data = int(input("Enter data: "))
                pos = int(input("Enter position (0-based): "))
                ll.insert_atPosition(data, pos)
            except ValueError:
                print("Invalid input.")

        elif choice == 4:
            ll.delete_atEnd()

        elif choice == 5:
            try:
                key = int(input("Enter element to search: "))
                ll.search(key)
            except ValueError:
                print("Please enter a number.")

        elif choice == 6:
            ll.display()

        elif choice == 7:
            data = int(input("Enter data: "))
            ll.insert_atBeginning_Circular(data)

        elif choice == 8:
            data = int(input("Enter data: "))
            ll.insert_atEnd_Circular(data)

        elif choice == 9:
            ll.display_circular()

        elif choice == 10:
            ll.is_circular = not ll.is_circular
            mode = "CIRCULAR" if ll.is_circular else "NORMAL"
            print(f"→ Switched to {mode} mode")

        elif choice == 11:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()