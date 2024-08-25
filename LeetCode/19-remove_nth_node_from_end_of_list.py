"""

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end
of the list and return its head.


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

"""

from data_structures import ListNode
    
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummyNode = ListNode(0, head)
    leftPointer = dummyNode
    rightPointer = head

    while n > 0 and rightPointer:
        rightPointer = rightPointer.next
        n -= 1
    
    while rightPointer:
        leftPointer = leftPointer.next
        rightPointer = rightPointer.next
    
    leftPointer.next = leftPointer.next.next

    return dummyNode.next
    
if __name__ == '__main__':
    linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    print("n =", n)
    print("Original List :", linkedList)
    print("Updated List  :", removeNthFromEnd(linkedList, n))