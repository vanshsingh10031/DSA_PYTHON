class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
N1 = Node(10)
N2 = Node(20)

# Linking Nodes
N1.next = N2

# Displaying Data
print(N1.data)
print(N1.next.data)


#Visualization of Linked List
print(f"N1: {id(N1)}") # Address of N1
print(f"N1.data: {N1.data}") # Data of N1 
print(f"N1.next: {id(N1.next)}") # Address of N2
print(f"N1.next.data: {N1.next.data}") # Data of N2        