from LinkedList import LinkedList

lst = LinkedList() # Create a linked list
lst.add(1) 
lst.add(2) 
lst.add(3) 
lst.add(-3) 

for e in lst:
    print(e, end = ' ')
print()

iterator = iter(lst) # Create an iterator
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("*" * 60)

lst = LinkedList()

# Add elements to the list
lst.add("America") # Add America to the list
print("(1)", lst)

lst.insert(0, "Canada") # Add Canada to the beginning of the list
print("(2)", lst)

lst.add("Russia") # Add Russia to the end of the list
print("(3)", lst)

lst.addLast("France") # Add France to the end of the list
print("(4)", lst)

lst.insert(2, "Germany") # Add Germany to the list at index 2
print("(5)", lst)

lst.insert(5, "Norway") # Add Norway to the list at index 5
print("(6)", lst)

lst.insert(0, "Poland") # Same as list.addFirst("Poland")
print("(7)", lst)

# Remove elements from the list
lst.removeAt(0) # Remove the element at index 0
print("(8)", lst)

lst.removeAt(2) # Remove the element at index 2
print("(9)", lst)

lst.removeAt(lst.getSize() - 1) # Remove the last element
print("(10)", lst)





# Test the LinkedList class
# Python Program of Traversal of Circular Linked List
class Node:
    def __init__(self, data):
        # Initialize a node with data and next pointer
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        # Initialize an empty circular linked list with head pointer pointing to None
        self.head = None

    def append(self, data):
        # Append a new node with data to the end of the circular linked list
        new_node = Node(data)
        if not self.head:
            # If the list is empty, make the new node point to itself
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                # Traverse the list until the last node
                current = current.next
            # Make the last node point to the new node
            current.next = new_node
            # Make the new node point back to the head
            new_node.next = self.head

    def traverse(self):
        # Traverse and display the elements of the circular linked list
        if not self.head:
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                # Break the loop when we reach the head again
                break

# Driver Code
circular_list = CircularLinkedList()
circular_list.append(1)
circular_list.append(2)
circular_list.append(3)

print("Traversing Circular Linked List:")
circular_list.traverse()