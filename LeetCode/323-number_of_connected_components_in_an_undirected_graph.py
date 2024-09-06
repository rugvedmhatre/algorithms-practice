"""

https://neetcode.io/problems/count-connected-components

There is an undirected graph with n nodes. There is also an 
edges array, where edges[i] = [a, b] means that there is an 
edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:
Input:
n=3
edges=[[0,1], [0,2]]
Output:
1

Example 2:
Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]
Output:
2

Constraints:
- 1 <= n <= 100
- 0 <= edges.length <= n * (n - 1) / 2

"""

def countComponents(n: int, edges: list[list[int]]) -> int:
    parents = [i for i in range(n)]
    rank = [1] * n

    def findRootParent(node1):
        result = node1

        while result != parents[result]:
            parents[result] = parents[parents[result]]
            result = parents[result]
        
        return result
    
    def unionComponents(node1, node2):
        parent1 = findRootParent(node1)
        parent2 = findRootParent(node2)

        if parent1 == parent2:
            return 0
        
        if rank[parent2] > rank[parent1]:
            parents[parent1] = parent2
            rank[parent2] += rank[parent1]
        else:
            parents[parent2] = parent1
            rank[parent1] += rank[parent2]
        
        return 1
    
    result = n
    for node1, node2 in edges:
        result -= unionComponents(node1, node2)
    
    return result

if __name__ == '__main__':
    n = 6
    edges=[[0,1], [1,2], [2,3], [4,5]]
    print(countComponents(n, edges))