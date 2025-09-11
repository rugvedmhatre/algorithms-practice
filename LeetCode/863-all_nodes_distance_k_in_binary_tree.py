"""

https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

Given the root of a binary tree, the value of a target node target, and an integer k, return an 
array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
 

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, 
and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:
- The number of nodes in the tree is in the range [1, 500].
- 0 <= Node.val <= 500
- All the values Node.val are unique.
- target is the value of one of the nodes in the tree.
- 0 <= k <= 1000

"""

from data_structures import TreeNode
from collections import defaultdict, deque

def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    if k == 0:
        return [target.val]
    
    graph = defaultdict(list)

    q = deque([root])

    while q:
        node = q.popleft()

        if node.left:
            graph[node].append(node.left)
            graph[node.left].append(node)

            q.append(node.left)
        
        if node.right:
            graph[node].append(node.right)
            graph[node.right].append(node)

            q.append(node.right)
    
    q = deque([(target, 0)])
    visited = set([target])
    
    result = []
    
    while q:
        node, dist = q.popleft()

        if dist == k:
            result.append(node.val)
        
        for e in graph[node]:
            if e not in visited:
                visited.add(e)
                q.append((e, dist + 1))
    
    return result

if __name__ == "__main__":
    # Test Case 1
    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), 
                    TreeNode(1, TreeNode(0), TreeNode(8)))
    target = root.left
    k = 2
    root.display()
    print(distanceK(root, target, k))

    # Test Case 2
    root = TreeNode(1)
    target = root
    k = 3
    root.display()
    print(distanceK(root, target, k))