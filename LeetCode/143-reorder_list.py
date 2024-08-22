"""

https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be 
represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes
themselves may be changed.


Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        head = self
        result = []
        while head != None:
            result.append(str(head.val))
            head = head.next
        return '[' + ','.join(result) + ']'

def reorderList(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slowPointer = head
    fastPointer = head.next

    while fastPointer and fastPointer.next:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    
    secondPointer = slowPointer.next
    slowPointer.next = None
    previousNode = None

    while secondPointer:
        nextNode = secondPointer.next
        secondPointer.next = previousNode
        previousNode = secondPointer
        secondPointer = nextNode
    
    firstPointer = head
    secondPointer = previousNode

    while secondPointer:
        firstNext = firstPointer.next
        secondNext = secondPointer.next
        firstPointer.next = secondPointer
        secondPointer.next = firstNext
        firstPointer = firstNext
        secondPointer = secondNext

if __name__ == '__main__':
    linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print("Original List:", linkedList)
    reorderList(linkedList)
    print("Reordered List:", linkedList)