"""

https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an 
integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order
that it is in).
 

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so 
the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:
- 1 <= k <= points.length <= 10^4
- -10^4 <= xi, yi <= 10^4

"""

import heapq

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    distances = []
    for x, y in points:
        distances.append(tuple([x**2 + y**2, [x, y]]))
    heapq.heapify(distances)
    
    result = []
    while k != 0:
        result.append(heapq.heappop(distances)[1])
        k -= 1

    return result

if __name__ == '__main__':
    # Test Case 1
    points = [[1,3],[-2,2]]
    k = 1
    print(kClosest(points, k))

    # Test Case 2
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(kClosest(points, k))