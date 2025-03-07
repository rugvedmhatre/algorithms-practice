"""

https://leetcode.com/problems/unique-number-of-occurrences/

Given an array of integers arr, return true if the number of occurrences of each value in the array is 
unique or false otherwise.


Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number 
of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000

"""

from collections import defaultdict

def uniqueOccurrences(arr: list[int]) -> bool:
    counts = defaultdict(int)
    for num in arr:
        counts[num] += 1

    sortedCounts = sorted(counts.values())

    for i in range(1, len(sortedCounts)):
        if sortedCounts[i - 1] == sortedCounts[i]:
            return False
    
    return True

if __name__ == '__main__':
    # Test case 1
    arr = [1,2,2,1,1,3]
    print(uniqueOccurrences(arr)) # Output: True

    # Test case 2
    arr = [1,2]
    print(uniqueOccurrences(arr)) # Output: False

    # Test case 3
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    print(uniqueOccurrences(arr)) # Output: True