# Introduction to Linked Lists
# Singly Linked List Operations -> Traversal, Append, Deletion, Insertion of Nodes in SLL

# How to Create a Node and SLL

# |5|618|-->|10|511|-->|7|997|-->|8|None|
#   787       618        511       997

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = Node(5) #5 is data
node2 = Node(10)
node3 = Node(7)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

print(node1)
print(node1.val)
print(node1.next)
print(node1.next.val)
print(node1.next.next.next)
print(node1.next.next.next.val)
