"""

https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:
- Choose any node in the binary tree and a direction (right or left).
- If the current direction is right, move to the right child of the current node; otherwise, move to 
  the left child.
- Change the direction from right to left or from left to right.
- Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.


Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
1_      
  \     
  1___  
 /    \ 
 1  __1 
   /   \
   1   1
    \   
    1   
     \  
     1 
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
      1 
     / \
 ____1 1
/       
1__     
   \    
  _1    
 /  \   
 1  1   
  \     
  1     
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0
 

Constraints:
- The number of nodes in the tree is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 100

"""

from data_structures import TreeNode

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.path = 0

        def dfs(node: TreeNode, wasLeft: bool, current_path: int):
            if node is None:
                return
            
            self.path = max(self.path, current_path)

            if wasLeft:
                dfs(node.right, False, current_path + 1)
                dfs(node.left, True, 1)
            else:
                dfs(node.right, False, 1)
                dfs(node.left, True, current_path + 1)
        
        dfs(root.right, False, 1)
        dfs(root.left, True, 1)

        return self.path

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    root = TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1, None, TreeNode(1, None, TreeNode(1))), TreeNode(1))))
    root.display()
    print(solution.longestZigZag(root))
    
    # Test Case 2
    root = TreeNode(1, TreeNode(1, TreeNode(1, None, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1)))), TreeNode(1))
    root.display()
    print(solution.longestZigZag(root))

    # Test Case 3
    root = TreeNode(1)
    root.display()
    print(solution.longestZigZag(root))
