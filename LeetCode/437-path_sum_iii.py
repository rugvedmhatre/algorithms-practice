"""

https://leetcode.com/problems/path-sum-iii/

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum 
of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., 
traveling only from parent nodes to child nodes).


Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:
- The number of nodes in the tree is in the range [0, 1000].
- -10^9 <= Node.val <= 10^9
- -1000 <= targetSum <= 1000

"""

from collections import Counter
from data_structures import TreeNode

def pathSum(root: TreeNode, targetSum: int) -> int:
    def dfs(node, current_sum):
        if node == None:
            return 0
        
        current_sum += node.val
        
        path_count = counter[current_sum -targetSum]
        
        counter[current_sum] += 1
        path_count += dfs(node.left, current_sum)
        path_count += dfs(node.right, current_sum)

        counter[current_sum] -= 1

        return path_count

    counter = Counter({0:1})

    return dfs(root, 0)

if __name__ == '__main__':
    # Test Case 1
    root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3),  TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
    targetSum = 8
    root.display()
    print(pathSum(root, targetSum))