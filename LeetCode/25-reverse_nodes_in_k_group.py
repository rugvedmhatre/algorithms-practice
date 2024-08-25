"""

https://leetcode.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list
k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length
of the linked list. If the number of nodes is not a multiple of
k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes
themselves may be changed.
 

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?

"""

from data_structures import ListNode

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        prev, current = kth.next, groupPrev.next
        while current != groupNext:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        nxt = groupPrev.next
        groupPrev.next = kth
        groupPrev = nxt
    
    return dummy.next

def getKth(current, k):
    while current and k > 0:
        current = current.next
        k -= 1
    return current

if __name__ == '__main__':
    linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    print("Original List :", linkedList)
    print("Updated List  :", reverseKGroup(linkedList, k = 2))