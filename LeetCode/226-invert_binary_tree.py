"""

https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return
its root. 

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
 

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

"""

# All commonly used data structures are initialised in 'datastructures.py'
from data_structures import TreeNode

def invertTree(root: TreeNode) -> TreeNode:
    if root == None:
        return
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

if __name__ == '__main__':
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    print("Original Tree:")
    root.display()
    print("")

    invertTree(root)
    print("Inverted Tree:")
    root.display()
