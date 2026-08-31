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
        
    def delete(self, val):
        temp = self.head
        
        # Check if list is empty
        if temp is None:
            print("Node not found")
            return
            
        # Check if head is the node to delete
        if temp.val == val:
            self.head = temp.next
            return
            
        found = False
        prev = None
        
        # Traverse to find the node and track 'prev'
        while temp is not None:
            if temp.val == val:
                found = True
                break
            prev = temp       # Update prev to current node
            temp = temp.next  # Move temp to next node
            
        # Perform deletion after loop finishes
        if found:
            prev.next = temp.next
            return
        else:
            print("Node not found") 


obj = SinglyLinkedList()
obj.head = node1
obj.delete(3)

current = obj.head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
print("None")