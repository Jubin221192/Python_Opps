# -*- coding: utf-8 -*-
"""

Created on Thu Aug 15 22:18:25 2019
@author: jubin


"""

# Linked List Implementation

class Node(object):
    
    def __init__(self,value, nextnode = None):
        self.value= value
        self.nextnode= nextnode
        
    def __str__(self):
        return str(self.value)

    

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

a.value

b.value

c.value

# printing the linked list in readable format
def linked_list_to_string(head):
    current = head
    str_list = []
    while current:
        str_list.append(str(current.value))
        current = current.nextnode
    str_list.append('(None)')
    return ' -> '.join(str_list)

# inserting values
current = Node(1)
for i in range(2, 8):
    current = Node(i, current)
head = current

linked_list_to_string(head)

# Finding the nth element
def nth_from_last(head, n):
    left = head
    right = head
    for i in range(n):
        if right == None:
            return None
        right = right.nextnode
    while right:
        right = right.nextnode
        left = left.nextnode
    return left

# Finding the nth element
print(nth_from_last(head,2))

# Reversing a linked List

def reverse(head):
    current = head
    previous = None
    nextnode = None
    
    while current:
        
        nextnode = current.nextnode
        
        current.nextnode = previous
        
        previous = current
        current = nextnode
        
    return previous

def print_nums(x):
    for i in range(x):
        print(i)
        return
    
print_nums(10)
        
        
while False:
    print("Looping...")        


from collections import Counter
Counter('abcdeabcdabcaba').most_common(6)


        
        
        
        
    
    



