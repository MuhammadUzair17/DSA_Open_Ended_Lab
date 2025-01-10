# Lab Task: Reverse a Linked List Using Stack
# Objective:
# Create a Python program that uses a stack to reverse a singly linked list.
# Problem Statement:
# Write a Python function reverse_linked_list(head: Node) -> Node that reverses a given singly linked list using a stack. You are given the head node of a singly linked list, and you need to return the head of the new reversed list.


# Here , i am defining the node class
class Node:
    # Creating a constructor  which accepts the value for the node 
    def __init__(self, value):  
        # Storing the value
        self.value = value      
        # initially, next is None
        self.next = None        

# Creating a Function to reverse the linked list using a stack
def reverse_linked_list(head: Node) -> Node:
     # If the list is empty, code will return None
    if not head: 
        return None
     # Stack to store nodes
    stack = []  
    current = head

    # Appending all nodes into the stack
    while current:
        stack.append(current)
        current = current.next

    # Popping the nodes to reverse the order
    new_head = stack.pop() 
    # The last node becomes the new head
    current = new_head

    # This loop will run till the stack is not empty and reversed list
    while stack:
        current.next = stack.pop()
        current = current.next

    # The last node is pointing to none
    current.next = None  
    return new_head

    # It is a Helper to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    # Creating the head node
    head = Node(values[0])  
    current = head

    # A loop to create the linked list
    for value in values[1:]:
        # Create the next node and link
        current.next = Node(value)  
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Input elements
list = create_linked_list([10,20,30,40,50])  
print("Original List:")
print_linked_list(list)

# Reversing the linked list
reversed_list = reverse_linked_list(list)
print("Reversed List:")
print_linked_list(reversed_list)
