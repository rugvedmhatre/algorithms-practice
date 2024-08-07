"""

https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k 
most frequent elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

from collections import defaultdict

def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequencies = defaultdict(int)
        
    for num in nums:
        frequencies[num] += 1
    
    sortedFrequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    result = []

    for i in range(k):
        result.append(sortedFrequencies[i][0])

    return result

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums, k))