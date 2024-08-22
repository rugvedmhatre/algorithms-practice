"""

https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains 
an additional random pointer, which could point to any node in 
the list, or null.

Construct a deep copy of the list. The deep copy should consist
of exactly n brand new nodes, where each new node has its value
set to the value of its corresponding original node. Both the
next and random pointer of the new nodes should point to new
nodes in the copied list such that the pointers in the original
list and copied list represent the same list state. None of the
pointers in the new list should point to nodes in the original
list.

For example, if there are two nodes X and Y in the original
list, where X.random --> Y, then for the corresponding two nodes
x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of
n nodes. Each node is represented as a pair of
[val, random_index] where:
- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) that 
  the random pointer points to, or null if it does not point to
  any node.

Your code will only be given the head of the original linked list.


Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random is null or is pointing to some node in the linked list.

"""

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
    
    def __str__(self):
        head = self
        result = []
        while head != None:
            result.append('[' + \
                ','.join([str(head.val), 
                          str(head.next.val if head.next else None), 
                          str(head.random.val if head.random else None)]) + \
                ']')
            head = head.next
        return '[' + ','.join(result) + ']'

def copyRandomList(head: ListNode) -> ListNode:
    oldToCopy = {None:None}

    current = head
    while current:
        copy = ListNode(current.val)
        oldToCopy[current] = copy
        current = current.next
    
    current = head
    while current:
        copy = oldToCopy[current]
        copy.next = oldToCopy[current.next]
        copy.random = oldToCopy[current.random]
        current = current.next
    
    return oldToCopy[head]

if __name__ == '__main__':
    linkedList = ListNode(7, ListNode(13, ListNode(11, ListNode(10, ListNode(1)))))

    randomPointer = {
        linkedList : None,
        linkedList.next : linkedList,
        linkedList.next.next : linkedList.next.next.next.next,
        linkedList.next.next.next : linkedList.next.next,
        linkedList.next.next.next.next : linkedList
    }

    current = linkedList
    while current:
        current.random = randomPointer[current]
        current = current.next
    
    print("Original List :", linkedList)
    print("Copied List   :", copyRandomList(linkedList))