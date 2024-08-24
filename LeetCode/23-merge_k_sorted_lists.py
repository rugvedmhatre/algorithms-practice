"""

https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list
is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and
return it.
 

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.

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

def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists or len(lists) == 0:
        return None
    
    while len(lists) > 1:
        mergedLists = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeList(l1, l2))
        
        lists = mergedLists
    
    return lists[0]

def mergeList(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1:
        tail.next = l1
    
    if l2:
        tail.next = l2
    
    return dummy.next

if __name__ == '__main__':
    lists = [
        ListNode(1, ListNode(4, ListNode(5))), 
        ListNode(1, ListNode(3, ListNode(4))), 
        ListNode(2, ListNode(6))
    ]
    print(mergeKLists(lists))