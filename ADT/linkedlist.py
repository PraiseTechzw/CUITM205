class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Points to the previous node
        self.next = None  # Points to the next node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head:  
            new_node.next = self.head  # Link new node to old head
            self.head.prev = new_node  # Link old head back to new node
        self.head = new_node  # New node becomes the head

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.insert_at_start(10)
dll.insert_at_start(20)
dll.insert_at_start(30)
dll.display()


'''2. Add an Element at the End of a Linked List
python
Copy
Edit
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Empty list at first

    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # If empty, new node is the head
            return
        temp = self.head
        while temp.next:  # Go to the last node
            temp = temp.next
        temp.next = new_node  # Add new node at the end

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
ll = LinkedList()
ll.add_at_end(5)
ll.add_at_end(15)
ll.add_at_end(25)
ll.display()
