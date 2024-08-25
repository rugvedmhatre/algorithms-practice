"""

https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the 
diameter of the tree.

The diameter of a binary tree is the length of the longest path
between any two nodes in a tree. This path may or may not pass
through the root.

The length of a path between two nodes is represented by the
number of edges between them.


Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100

"""

from data_structures import TreeNode

def dfs(current: TreeNode, result) -> int:
    if current == None:
        return 0, result
    
    left, _ = dfs(current.left, result)
    right, _ = dfs(current.right, result)
    
    result = max(result, left + right)

    return 1 + max(left, right), result

def diameterOfBinaryTree(root: TreeNode) -> int:
    _, result = dfs(root, 0)
    return result

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    # root = TreeNode(1, TreeNode(2))
    print("Original Tree:")
    root.display()
    print("Tree Diameter :", diameterOfBinaryTree(root))