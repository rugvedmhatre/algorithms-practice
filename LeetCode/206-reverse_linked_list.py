"""

https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, 
and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively
or recursively. Could you implement both?

"""

from data_structures import ListNode

def reverseList(head: ListNode) -> ListNode:
    prev = None
    
    while head != None:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    
    return prev

if __name__ == '__main__':
    linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original List:", linkedList)
    print("Reversed List:", reverseList(linkedList))