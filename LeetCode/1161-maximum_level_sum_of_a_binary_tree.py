"""

https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and 
so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5

"""

from data_structures import TreeNode

def maxLevelSum(root: TreeNode) -> int:
    curr_level = 1
    max_sum = root.val
    level = [root]
    max_level = 1

    while level != []:
        next_level = []
        level_sum = 0
        curr_level += 1
        for node in level:
            if node.left:
                next_level.append(node.left)
                level_sum += node.left.val
            if node.right:
                next_level.append(node.right)
                level_sum += node.right.val
        if next_level != [] and level_sum > max_sum:
            max_sum = level_sum
            max_level = curr_level
        level = next_level
    
    return max_level

if __name__ == '__main__':
    # Test Case 1
    root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
    print(maxLevelSum(root))