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


head = node1

slow = head
fast = head
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

print(slow.val)

# TC -> O(N/2)
# SC -> O(1)