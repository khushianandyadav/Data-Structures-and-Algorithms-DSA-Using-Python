# 1. SLL can be empty.
# 2. SLL is not empty.

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


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

obj = SinglyLinkedList()
obj.head = node1 
obj.append(20)

print(node4.next.val)

# TC -> O(N)
# SC -> O(1)