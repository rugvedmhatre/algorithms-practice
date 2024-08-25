"""

https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
 

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -10^4 <= Node.val <= 10^4

"""

from data_structures import TreeNode

def dfs(root: TreeNode) -> list:
    if root == None:
        return [True, 0]
    
    left, right = dfs(root.left), dfs(root.right)
    balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

    return [balanced, 1 + max(left[1], right[1])]

def isBalanced(root: TreeNode) -> bool:    
    return dfs(root)[0]

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    # root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    print("Original Tree:")
    root.display()
    print("Is Tree Balanced:")
    print(isBalanced(root))