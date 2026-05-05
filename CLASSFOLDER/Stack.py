class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # PUSH → O(1)
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} pushed to stack")

    # POP → O(1)
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None

        popped_data = self.top.data
        self.top = self.top.next
        print(f"{popped_data} popped from stack")
        return popped_data

    # PEEK → O(1)
    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None

        print(f"Top element is: {self.top.data}")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        current = self.top
        print("Stack elements (TOP → BOTTOM):")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# ──────────────────────────────── MAIN MENU ────────────────────────────────
def main():
    stack = Stack()

    while True:
        print("\n===== STACK OPERATIONS =====")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Check if Empty")
        print("6. Exit")

        try:
            choice = int(input("\nEnter choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                data = int(input("Enter data: "))
                stack.push(data)
            except ValueError:
                print("Invalid data.")

        elif choice == 2:
            stack.pop()

        elif choice == 3:
            stack.peek()

        elif choice == 4:
            stack.display()

        elif choice == 5:
            if stack.is_empty():
                print("Stack is empty")
            else:
                print("Stack is NOT empty")

        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()