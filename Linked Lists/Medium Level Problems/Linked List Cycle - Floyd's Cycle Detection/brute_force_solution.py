# Part 59 Linked List (Medium Level Problems)
# LeetCode 141 - Linked List Cycle - Floyd's Cycle Detection

# Check whether there is a cycle

# EXAMPLE 1
# 5 -> 9 -> 1 -> 7 -> 6 -> 4 -> 9 -> 2 -> 8 -> 1
# -> True


# EXAMPLE 2
# 5 -> 9 -> 8 -> 4 -> 6 -> 7 -> None
# -> False

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
node5.next = node2

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def cycle(self):
        temp = self.head
        my_set = set()
        while temp is not None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp = temp.next
        return False



obj = SinglyLinkedList()
obj.head = node1
print(obj.cycle())
