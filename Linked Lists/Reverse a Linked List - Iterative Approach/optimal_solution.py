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

    def reverse(self):

        temp = self.head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        self.head = prev


obj = SinglyLinkedList()
obj.head = node1
obj.reverse()

current = obj.head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
print("None")

# TC -> O(N)
# SC -> O(1)