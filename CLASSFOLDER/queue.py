import array as arr

class Queue:
    def __init__(self, capacity):
        self.items = arr.array('i', [])
        self.capacity = capacity

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity

    def enqueue(self, x):
        if self.is_full():
            print("❌ Queue is full. Cannot enqueue.")
            return
        
        self.items.append(x)
        print(f"✅ {x} added to queue.")

    def dequeue(self):
        if self.is_empty():
            print("❌ Queue is empty. Cannot dequeue.")
            return
        
        removed = self.items.pop(0)
        print(f"✅ {removed} removed from queue.")

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(f"Front element: {self.items[0]}")

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        
        print("Queue:", end=" ")
        for item in self.items:
            print(item, end=" -> ")
        print("None")


# =========================
# MENU DRIVEN PROGRAM
# =========================
if __name__ == "__main__":
    capacity = int(input("Enter queue capacity: "))
    q = Queue(capacity)

    while True:
        print("\n--- Queue Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Print Queue")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            value = int(input("Enter value to enqueue: "))
            q.enqueue(value)

        elif choice == '2':
            q.dequeue()

        elif choice == '3':
            q.peek()

        elif choice == '4':
            q.print_queue()

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("❌ Invalid choice. Try again.")