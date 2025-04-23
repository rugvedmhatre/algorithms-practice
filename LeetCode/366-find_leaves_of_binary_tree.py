"""

https://leetcode.com/problems/find-leaves-of-binary-tree/

Given the root of a binary tree, collect a tree's nodes as if you were doing this:
- Collect all the leaf nodes.
- Remove all the leaf nodes.
- Repeat until the tree is empty.

Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it
does not matter the order on which elements are returned.

Example 2:
Input: root = [1] Output: [[1]]

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- -100 <= Node.val <= 100

"""

from data_structures import TreeNode
from collections import defaultdict

def findLeaves(root: TreeNode) -> list[list[int]]:
    leaves_map = defaultdict(list)
    
    def dfs(node, layer):
        if not node:
            return layer
        
        left = dfs(node.left, layer)
        right = dfs(node.right, layer)

        layer = max(left, right)

        leaves_map[layer].append(node.val)

        return layer + 1
    
    dfs(root, 0)

    return leaves_map.values()


if __name__ == "__main__":
    # Test Case 1
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    root.display()
    print(findLeaves(root))

    # Test Case 2
    root = TreeNode(1)
    root.display()
    print(findLeaves(root))