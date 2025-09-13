"""

https://leetcode.com/problems/most-frequent-subtree-sum/

Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return 
all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree 
rooted at that node (including the node itself).

Example 1:
Input: root = [5,2,-3]
Output: [2,-3,4]

Example 2:
Input: root = [5,2,-5]
Output: [2]

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5

"""

from data_structures import TreeNode
from collections import defaultdict

def findFrequentTreeSum(root: TreeNode) -> list[int]:
    subtree_sums = defaultdict(int)

    def dfs(node):
        if not node:
            return 0
        
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)

        total_sum = left_sum + node.val + right_sum
        subtree_sums[total_sum] += 1

        return total_sum
    
    dfs(root)

    max_count = max(subtree_sums.values())
    
    result = []

    for total_sum, count in subtree_sums.items():
        if count == max_count:
            result.append(total_sum)

    return result

if __name__ == "__main__":
    # Test Case 1
    root = TreeNode(5, TreeNode(2), TreeNode(-3))
    root.display()
    print(findFrequentTreeSum(root))

    # Test Case 2
    root = TreeNode(5, TreeNode(2), TreeNode(-5))
    root.display()
    print(findFrequentTreeSum(root))