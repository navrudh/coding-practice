"""
Data Structures > Linked Lists > Print the Elements of a Linked List

"""

def print_list(head):
    if head != None:
        print(head.data)
        print_list(head.next)
        