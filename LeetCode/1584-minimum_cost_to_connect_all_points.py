"""

https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array points representing integer coordinates 
of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the
manhattan distance between them: |xi - xj| + |yi - yj|, where 
|val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All 
points are connected if there is exactly one simple path 
between any two points.


Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:
- 1 <= points.length <= 1000
- -10^6 <= xi, yi <= 10^6
- All pairs (xi, yi) are distinct.

"""

from collections import defaultdict
import heapq

def minCostConnectPoints(points: list[list[int]]) -> int:
    N = len(points)

    adj = defaultdict(list)

    for i in range(N):
        x1, y1 = points[i]

        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x1- x2) + abs(y1- y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])
    
    result = 0
    visited = set()
    minHeap = [[0, 0]]

    while len(visited) < N:
        cost, i = heapq.heappop(minHeap)

        if i in visited:
            continue
            
        result += cost
        visited.add(i)

        for adjCost, adjPoint in adj[i]:
            if adjPoint not in visited:
                heapq.heappush(minHeap, [adjCost, adjPoint])
        
    return result

if __name__ == '__main__':
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(minCostConnectPoints(points))