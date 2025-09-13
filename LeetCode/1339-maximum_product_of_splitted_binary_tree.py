"""

https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such
that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, 
return it modulo 10^9 + 7.

Note: You need to maximize the answer before taking the modulo.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove one edge to get two binary trees with sums 11 and 10. Their product is 110 
(11*10).

Example 2:
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove one edge to get two binary trees with sums 15 and 6. Their product is 90 
(15*6).

Constraints:
- The number of nodes in the tree is in the range [2, 5 * 10^4].
- 1 <= Node.val <= 10^4

"""

from data_structures import TreeNode

def maxProduct(root: TreeNode) -> int:
    treesums = []

    def dfs(node):
        if not node:
            return 0
        
        lsum = dfs(node.left)
        rsum = dfs(node.right)

        cur_sum = lsum + rsum + node.val

        treesums.append(cur_sum)

        return cur_sum
    
    totalsum = dfs(root)

    max_product = 0

    for treesum in treesums:
        product = treesum * (totalsum - treesum)
        max_product = max(max_product, product)
    
    return max_product % (10**9 + 7)

if __name__ == "__main__":
    # Test Case 1
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    root.display()
    print(maxProduct(root))

    # Test Case 2
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5), TreeNode(6))))
    root.display()
    print(maxProduct(root))