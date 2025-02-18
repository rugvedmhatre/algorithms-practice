"""

https://leetcode.com/problems/odd-even-linked-list/

Given the head of a singly linked list, group all the nodes with 
odd indices together followed by the nodes with even indices, 
and return the reordered list.

The first node is considered odd, and the second node is even, 
and so on.

Note that the relative order inside both the even and odd groups
should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and 
O(n) time complexity.


Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:
- The number of nodes in the linked list is in the range [0, 10^4].
- -10^6 <= Node.val <= 10^6

"""

from data_structures import ListNode

def oddEvenList(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    
    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_head
    
    return head

if __name__ == '__main__':
    # Test Case 1
    print("Test Case 1")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(head)
    head = oddEvenList(head)
    print(head)

    print("\nTest Case 2")
    head = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    print(head)
    head = oddEvenList(head)
    print(head)