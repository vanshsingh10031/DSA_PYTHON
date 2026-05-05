class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        print(f"\nPushing {x} into stack...")
        print(self.top)
        temp = Node(x)
        temp.next = self.top
        self.top = temp
        print(self.top)
        print("Stack after push:")
        self.print_stack()

    def print_stack(self):
        temp = self.top
        if temp is None:
            print("Stack is empty")
            return
        
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---- MAIN ----
if __name__ == "__main__":
    s = Stack()

    # Step-by-step pushes
    s.push(10)
    s.push(20)
    s.push(30)