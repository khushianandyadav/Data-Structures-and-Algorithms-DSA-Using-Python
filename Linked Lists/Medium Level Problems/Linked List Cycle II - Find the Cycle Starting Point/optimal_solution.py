# Part 60 Linked Lists(Medium Level Problems)
# LeetCode 142: Linked List Cycle II
# Find the Cycle Starting Point

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
node5.next = node3

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def f_cycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.val
        return None




obj = SinglyLinkedList()
obj.head = node1
print(obj.f_cycle())

#TC -> O(N)
#SC -> O(1)
