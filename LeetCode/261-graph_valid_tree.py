"""

https://neetcode.io/problems/valid-tree

Given n nodes labeled from 0 to n - 1 and a list of undirected 
edges (each edge is a pair of nodes), write a function to check
whether these edges make up a valid tree.


Example 1:
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output:
true

Example 2:
Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output:
false

Note:
- You can assume that no duplicate edges will appear in edges. 
  Since all edges are undirected, [0, 1] is the same as [1, 0]
  and thus will not appear together in edges.

Constraints:
- 1 <= n <= 100
- 0 <= edges.length <= n * (n - 1) / 2

"""

def validTree(n: int, edges: list[list[int]]) -> bool:
    if not n:
        return True
    
    adj = {i : [] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    visited = set()

    def dfs(i, prev):
        if i in visited:
            return False
        
        visited.add(i)

        for j in adj[i]:
            if j == prev:
                continue
            if not dfs(j, i):
                return False
        
        return True
    
    return dfs(0, -1) and n == len(visited)

if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(validTree(n, edges))