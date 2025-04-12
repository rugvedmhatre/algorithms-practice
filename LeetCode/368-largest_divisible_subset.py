"""

https://leetcode.com/problems/largest-divisible-subset/

Given a set of distinct positive integers nums, return the largest subset answer such that every 
pair (answer[i], answer[j]) of elements in this subset satisfies:
- answer[i] % answer[j] == 0, or
- answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.
 

Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]


Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 2 * 10^9
- All the integers in nums are unique.

"""
# import time

# DFS Approach
def largestDivisibleSubset(nums: list[int]) -> list[int]:
    nums.sort()
    cache = {}

    def dfs(i):
        if i == len(nums):
            return []
        
        if i in cache:
            return cache[i]
        
        result = [nums[i]]
        for j in range(i+1, len(nums)):
            if nums[j] % nums[i] == 0:
                tmp = [nums[i]] + dfs(j)
                if len(tmp) > len(result):
                    result = tmp
        cache[i] = result
        return result
    
    result = []
    for i in range(len(nums)):
        tmp = dfs(i)
        if len(tmp) > len(result):
            result = tmp
    
    return result

# DP Approach
def largestDivisibleSubsetDP(nums: list[int]) -> list[int]:
    nums.sort()
    dp = [[n] for n in nums]
    result = []

    for i in reversed(range(len(nums))):
        for j in range(i+1, len(nums)):
            if nums[j] % nums[i] == 0:
                tmp = [nums[i]] + dp[j]
                dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
        result = dp[i] if len(dp[i]) > len(result) else result
    
    return result

if __name__ == "__main__":
    # Test Case 1
    nums = [1,2,3]
    print(largestDivisibleSubset(nums))
    print(largestDivisibleSubsetDP(nums))
    
    # Test Case 2
    nums = [1, 2, 4, 8]
    print(largestDivisibleSubset(nums))
    print(largestDivisibleSubsetDP(nums))

# if __name__ == "__main__":
#     # Test Case 1
#     nums = [1,2,3]
    
#     start_time = time.perf_counter()
#     print(largestDivisibleSubset(nums))
#     end_time = time.perf_counter()
#     execution_time_dfs = end_time - start_time
#     print(f"Execution time: {execution_time_dfs} seconds")

#     start_time = time.perf_counter()
#     print(largestDivisibleSubsetDP(nums))
#     end_time = time.perf_counter()
#     execution_time_dp = end_time - start_time
#     print(f"Execution time: {execution_time_dp} seconds")
#     print(f"DP approach is faster by {(((execution_time_dfs - execution_time_dp) / execution_time_dfs) * 100):.2f}%")

#     # Test Case 2
#     nums = [1, 2, 4, 8]
#     print(largestDivisibleSubset(nums))
#     print(largestDivisibleSubsetDP(nums))