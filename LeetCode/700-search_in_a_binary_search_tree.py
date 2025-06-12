"""

https://leetcode.com/problems/search-in-a-binary-search-tree/

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that 
node. If such a node does not exist, return null. 

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []
 
Constraints:
- The number of nodes in the tree is in the range [1, 5000].
- 1 <= Node.val <= 10^7
- root is a binary search tree.
- 1 <= val <= 10^7

"""

from data_structures import TreeNode

def searchBST(root: TreeNode, val: int) -> TreeNode:

    def binarySearch(node : TreeNode, val: int):
        if node is None:
            return

        if node.val == val:
            return node
        elif node.val > val:
            return binarySearch(node.left, val)
        elif node.val < val:
            return binarySearch(node.right, val)
    
    return binarySearch(root, val)

if __name__ == "__main__":
    # Test Case 1
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    root.display()
    val = 2
    result = searchBST(root, val)
    if result is not None:
        result.display()

    # Test Case 2
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    root.display()
    val = 5
    result = searchBST(root, val)
    if result is not None:
        result.display()