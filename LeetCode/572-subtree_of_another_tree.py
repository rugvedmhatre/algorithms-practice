"""

https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return 
true if there is a subtree of root with the same structure and
node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a
node in tree and all of this node's descendants. The tree tree
could also be considered as a subtree of it


Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:
- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4

"""

from data_structures import TreeNode

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not subRoot:
        return True
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    
    return (isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot))

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    
    if p and q and p.val == q.val:
        return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))
    
    return False

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    print("Tree:")
    root.display()
    print("")
    print("Sub Tree:")
    subRoot.display()
    print("")
    print("Is Sub Tree :", isSubtree(root, subRoot))