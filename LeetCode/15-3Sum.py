"""

https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate 
triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

"""

def threeSum(nums: list[int]) -> list[list[int]]:
    result = list()
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        leftIdx = i + 1
        rightIdx = len(nums) - 1
        while leftIdx < rightIdx:
            threeSumVal = num + nums[leftIdx] + nums[rightIdx]
            if threeSumVal < 0:
                leftIdx += 1
            elif threeSumVal > 0:
                rightIdx -= 1
            else:
                result.append([num, nums[leftIdx], nums[rightIdx]])
                leftIdx += 1
                while nums[leftIdx] == nums[leftIdx - 1] and leftIdx < rightIdx:
                    leftIdx += 1
    
    return result

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))