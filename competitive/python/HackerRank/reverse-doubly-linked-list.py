"""
 Data Structures > Linked Lists > Reverse a doubly linked list

"""

def Reverse(head):
    if head is None:
        return head
    current = head
    while current is not None:
        next = current.next
        prev, current.next, current.prev = current, current.prev, current.next
        current = next
    return prev