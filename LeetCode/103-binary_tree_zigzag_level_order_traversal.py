"""

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100

"""

from collections import deque
from data_structures import TreeNode

def zigzagLevelOrder(root: TreeNode) -> list[list[int]]:
    result = []

    if root is None:
        return result

    q = deque([root])
    right = True

    while q:
        level = []

        for _ in range(len(q)):
            if right:
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                node = q.pop()
                level.append(node.val)
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)
        
        right = not right

        result.append(level)
    
    return result

if __name__ == "__main__":
    # Test Case 1
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    root.display()
    print(zigzagLevelOrder(root))

    # Test Case 2
    root = TreeNode(1)
    root.display()
    print(zigzagLevelOrder(root))

    # Test Case 3
    root = None
    print(zigzagLevelOrder(root))