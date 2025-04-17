"""

https://leetcode.com/problems/count-the-number-of-good-subarrays/

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and 
arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.
 

Example 1:
Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.

Example 2:
Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
 

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i], k <= 10^9

"""

from collections import defaultdict

def countGood(nums: list[int], k: int) -> int:
    count = 0
    l = 0
    
    cur_k = 0
    window = defaultdict(int)

    for r in range(len(nums)):
        cur_k += window[nums[r]]
        window[nums[r]] += 1

        while cur_k >= k:
            window[nums[l]] -= 1
            cur_k -= window[nums[l]]
            l += 1
        
        count += l
    
    return count

if __name__ == "__main__":
    # Test Case 1
    nums = [1,1,1,1,1]
    k = 10
    print(countGood(nums, k))

    # Test Case 2
    nums = [3,1,4,3,2,2,4]
    k = 2
    print(countGood(nums, k))