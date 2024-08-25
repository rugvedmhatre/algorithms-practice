"""

https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function
to check if they are the same or not.

Two binary trees are considered the same if they are
structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4

"""

from data_structures import TreeNode

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    
    if not p or not q or p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

if __name__ == '__main__':
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    print("Tree 1: ")
    p.display()
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    print("Tree 2: ")
    q.display()
    print("Is Same Tree?")
    print(isSameTree(p, q))