"""

https://leetcode.com/problems/leaf-similar-trees/

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a 
leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], 
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false


Constraints:
- The number of nodes in each tree will be in the range [1, 200].
- Both of the given trees will have values in the range [0, 200].

"""

from data_structures import TreeNode

def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
    leaves1 = []
    findLeaves(root1, leaves1)

    leaves2 = []
    findLeaves(root2, leaves2)

    return leaves1 == leaves2

def findLeaves(root: TreeNode, result: list[int]):
    if root == None:
        return
    
    if root.left == None and root.right == None:
        result.append(root.val)
    
    findLeaves(root.left, result)
    findLeaves(root.right, result)

if __name__ == '__main__':
    # Test Case 1
    root1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
    root2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))
    root1.display()
    root2.display()
    print(leafSimilar(root1, root2))

    # Test Case 2
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(3), TreeNode(2))
    root1.display()
    root2.display()
    print(leafSimilar(root1, root2))