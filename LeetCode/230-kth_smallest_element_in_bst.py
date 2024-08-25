"""

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values
of the nodes in the tree.
 

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4
 

Follow up: If the BST is modified often (i.e., we can do
insert and delete operations) and you need to find the
kth smallest frequently, how would you optimize?

"""

from data_structures import TreeNode

def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print("Tree:")
    root.display()
    print("")
    k = 1
    print(f"Kth Smallest Element in BST (k = {k})")
    print(kthSmallest(root, k))