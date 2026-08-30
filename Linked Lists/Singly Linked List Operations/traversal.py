# Head
#  |
#  v
# |5|117|-->|10|264|-->|3|851|-->|2|None|
#  819       117        264       851

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = Node(5)
node2 = Node(10)
node3 = Node(3)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def traversal(self):
        if self.head is None:
            print("SLL is empty.")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end = " ")
                curr = curr.next

obj = SinglyLinkedList()
obj.head = node1
obj.traversal()

# TC -> O(N)
# SC -> O(1)