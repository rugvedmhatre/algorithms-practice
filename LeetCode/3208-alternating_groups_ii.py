"""

https://leetcode.com/problems/alternating-groups-ii/

There is a circle of red and blue tiles. You are given an array of integers colors and an integer k.
The color of tile i is represented by colors[i]:
- colors[i] == 0 means that tile i is red.
- colors[i] == 1 means that tile i is blue.

An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in
the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next 
to each other.

Example 1:
Input: colors = [0,1,0,1,0], k = 3
Output: 3

Example 2:
Input: colors = [0,1,0,0,1,0,1], k = 6
Output: 2

Example 3:
Input: colors = [1,1,0,1], k = 4
Output: 0

Constraints:
- 3 <= colors.length <= 10^5
- 0 <= colors[i] <= 1
- 3 <= k <= colors.length

"""

def numberOfAlternatingGroups(colors: list[int], k: int) -> int:
    colors = colors + colors[:(k-1)]
    groups = 0
    l = 0

    for r in range(len(colors)):
        if r > 0 and colors[r] == colors[r-1]:
            l = r

        if r - l + 1 >= k:
            groups += 1

    return groups

if __name__ == '__main__':
    # Test Case 1
    colors = [0,1,0,1,0]
    k = 3
    print(numberOfAlternatingGroups(colors, k))

    # Test Case 2
    colors = [0,1,0,0,1,0,1]
    k = 6
    print(numberOfAlternatingGroups(colors, k))

    # Test Case 3
    colors = [1,1,0,1]
    k = 4
    print(numberOfAlternatingGroups(colors, k))
