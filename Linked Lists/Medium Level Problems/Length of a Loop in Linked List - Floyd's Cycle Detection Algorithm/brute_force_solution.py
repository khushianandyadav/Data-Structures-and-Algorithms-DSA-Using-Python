'''
Part 61 Linked Lists(Medium Level Problems)
Length of a Loop in Linked List - Floyd's Cycle Detection Algorithm
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def len_loop(self):
    temp = head
    travel = 0
    my_dict = dict()
    while temp is not None:
        if temp in my_dict:
            return travel - my_dict[temp]

        my_dict[temp] = travel
        travel += 1
        temp = temp.next
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
SC -> O(N)
'''

'''
Output:-
PS D:\DSA Using Python\Linked Lists\Medium Level Problems\Length of a Loop in Linked List - Floyd's Cycle Detection Algorithm> & "C:\Users\Khushi A Yadav\AppData\Local\Programs\Python\Python313\python.exe" "d:/DSA Using Python/Linked Lists/Medium Level Problems/Length of a Loop in Linked List - Floyd's Cycle Detection Algorithm/brute_force_solution.py"
5 9 1 7 6 1 9 2 8
Enter loop position (-1 for none):- 2
7
PS D:\DSA Using Python\Linked Lists\Medium Level Problems\Length of a Loop in Linked List - Floyd's Cycle Detection Algorithm> 
'''
