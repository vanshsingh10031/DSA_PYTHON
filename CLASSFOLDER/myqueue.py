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

    def insert(self, x):
        if self.is_full():
            print("Queue is FULL. Cannot insert.")
            return
        self.items.append(x)
        print("Inserted into Queue")

    def delete(self):
        if self.is_empty():
            print("Queue is EMPTY. Cannot delete.")
            return
        removed = self.items.pop(0)
        print(f"Deleted element: {removed}")

    def peek(self):
        return self.items[0]

    def print_queue(self):
        if self.is_empty():
            print("Queue is EMPTY")
            return
        print("Queue:", list(self.items))


def main():
    ll = Queue(5)

    while True:
        print("\n===== Queue Operations =====")
        print("1. Insert")
        print("2. Delete")
        print("3. Peek")
        print("4. Print Queue")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            value = int(input("Enter value to insert: "))
            ll.insert(value)

        elif choice == 2:
            ll.delete()

        elif choice == 3:
            ll.peek()

        elif choice == 4:
            ll.print_queue()

        elif choice == 5:
            print("Exiting")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()