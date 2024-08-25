"""

https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.
 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
 

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100

"""

from data_structures import TreeNode
from collections import deque

# recursive method
def maxDepth(root: TreeNode) -> int:
    if root == None:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# iterative bfs method
def maxDepthBFS(root: TreeNode) -> int:
    q = deque()
    if root:
        q.append(root)
    
    level = 0

    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    
    return level

# iterative dfs
def maxDepthDFS(root: TreeNode) -> int:
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth+1])
            stack.append([node.right, depth+1])
    
    return res

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("Original Tree:")
    root.display()
    print("Tree Depth :", maxDepth(root))