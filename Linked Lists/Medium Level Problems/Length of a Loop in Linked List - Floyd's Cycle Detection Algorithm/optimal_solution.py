class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def len_loop(self):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            count = 1
            while slow != fast:
                slow = slow.next
                count += 1
            return count
    return 0

def build_linked_list(values, pos):
    head = None
    tail = None
    nodes = []
    for v in values:
        node = Node(v)
        nodes.append(node)
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    if pos != -1:
        tail.next = nodes[pos]
    return head

values = list(map(int, input().split()))
pos = int(input("Enter loop position (-1 for none):- "))
head = build_linked_list(values, pos)


print(len_loop(head))

'''
TC -> O(N)
SC -> O(1)
'''