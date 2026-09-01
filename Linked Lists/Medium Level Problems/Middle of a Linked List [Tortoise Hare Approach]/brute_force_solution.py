# LeetCode 876 Linked Lists(Medium Level Problems)
# Middle of a Linked List [Tortoise-Hare Approach]

# In case of even length, return the second middle

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

n = 0
temp = head
while temp is not None:
    n+=1
    temp = temp.next

temp = head
for i in range(0, n//2):
    temp = temp.next

print(temp.val)

# TC -> O(N + N/2)
# SC -> O(1)
