"""
 Data Structures > Linked Lists > Insert a node into a sorted doubly linked list

"""
def SortedInsert(head, data):
    if head is None:
        return Node(data)
    if data <= head.data:
        head.prev = Node(data, head)
        return head.prev
    else:
        head.next = SortedInsert(head.next, data)
        head.next.prev = head
        return head
