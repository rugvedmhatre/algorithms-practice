"""

https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on
the right side of it, return the values of the nodes you can
see ordered from top to bottom.
 

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
 

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

"""

from data_structures import TreeNode
from collections import deque

def rightSideView(root: TreeNode) -> list[int]:
    result = []

    q = deque()
    q.append(root)

    while q:
        rightSide = None
        for i in range(len(q)):
            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        if rightSide:
            result.append(rightSide.val)
    return result

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print("Tree:")
    root.display()
    print("")
    print("Right Side View of the Tree :", rightSideView(root))