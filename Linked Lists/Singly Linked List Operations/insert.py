class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = Node(5)
node2 = Node(10)
node3 = Node(21)
node4 = Node(17)
node5 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current


obj = SinglyLinkedList()
obj.head = node1
obj.insert_at(13, 2)

current = obj.head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
print("None")